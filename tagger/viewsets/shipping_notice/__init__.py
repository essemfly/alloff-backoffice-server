from datetime import datetime

import pandas as pd
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets, mixins, status, fields, serializers, parsers
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from tagger.core.mongo.models.order import OrderStatus
from tagger.models import ShippingNotice, Package, Courier
from tagger.models.package import PackageStatus
from tagger.models.shipping_notice import ShippingNoticeStatus
from tagger.serializers.shipping import ShippingNoticeSerializer
from tagger.viewsets.order import ChangeStatusSerializer
from tagger.viewsets.order.change_status import _change_status
from tagger.viewsets.shipping_notice.make_shipping_notice import make_shipping_notice
from tagger.viewsets.shipping_notice.seal_package import seal_package
from tagger.viewsets.shipping_notice.template import make_cj_workbook


class ExcelUploaderRequestSerializer(serializers.Serializer):
    file = fields.FileField(required=True)
    notice_id = fields.CharField(required=True)


class ShippingNoticeResultUploaderViewSet(viewsets.GenericViewSet):
    serializer_class = ExcelUploaderRequestSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser, parsers.FileUploadParser, ]

    @extend_schema(
        responses={status.HTTP_200_OK: ShippingNoticeSerializer}
    )
    @action(methods=["POST"], detail=False)
    def upload(self, request):
        serializer = self.get_serializer(data=request.data)  # type: ImageUploaderRequestSerializer
        serializer.is_valid(raise_exception=True)

        file = serializer.validated_data.get("file")  # type: InMemoryUploadedFile
        notice_id = serializer.validated_data.get("notice_id")  # type: InMemoryUploadedFile
        notice = ShippingNotice.objects.filter(id=notice_id).first()

        if notice is None:
            raise APIException(f"No shipping notice found with id {notice_id}")
        if notice.status != ShippingNoticeStatus.SEALED:
            raise APIException("Only SEALED shipping notice can be shipped")

        courier = Courier.objects.filter(name="CJ대한통운").first()
        if courier is None:
            raise APIException("Courier not found")

        try:
            df = pd.read_html(file, match='주소', header=0)[0]
        except ValueError:
            raise APIException("Malformed Excel!")

        df = df.dropna(subset=["주문번호", "상태"]).astype(str)
        if {row["주문번호"] for _, row in df.iterrows()} != {x.code for x in notice.packages.all()}:
            raise APIException("Package codes do not match!")

        for _, row in df.iterrows():
            tracking_number = row['송장번호']
            if "." in tracking_number:
                # DataFrame float -> str issue
                tracking_number = tracking_number.split(".")[0]
            package = Package.objects.get(code=row["주문번호"])
            package.courier = courier
            package.tracking_number = tracking_number
            package.status = PackageStatus.SHIPPED
            package.save()

            for eo in package.extended_orders:
                order = eo.order
                status_change_data = {
                    "status": OrderStatus.DELIVERY_STARTED,
                    "delivery_tracking_number": package.courier.name + " " + package.tracking_number,
                    "delivery_tracking_url": package.tracking_url,
                }
                s = ChangeStatusSerializer(data=status_change_data, instance=order)
                s.is_valid(raise_exception=True)
                _change_status(s, order, User.objects.get(username="backoffice_server"), id=str(order.id))
                print("-----------------------------------------------------------------------")
                print(f"""[{package.code}] {package.recipient_name} ({package.recipient_mobile})""")
                for item in package.shipping_notice_items.all():
                    print(f"ㄴ https://office.alloff.co/orders/{item.item.extended_order.order.code}")
                    print(f"""   [INV {item.inventory.code}] {item.item.name}""")

        notice.status = ShippingNoticeStatus.SHIPPED
        notice.save()

        return Response(
            ShippingNoticeSerializer(notice).data,
            status=status.HTTP_200_OK
        )


class ShippingNoticeViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ShippingNotice.objects.order_by("-id")

    def list(self, request, *args, **kwargs):
        make_shipping_notice()
        return super().list(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action == "upload_cj_result":
            return ExcelUploaderRequestSerializer
        return ShippingNoticeSerializer

    @extend_schema(
        request=None,
        parameters=[OpenApiParameter("id", OpenApiTypes.STR, OpenApiParameter.PATH)],  # path variable was overridden
    )
    @action(detail=True, url_path="make-upload-template", methods=["POST"])
    def make_upload_template(self, request: Request, pk=None):
        notice = self.get_object()  # type: ShippingNotice
        if notice.status != ShippingNoticeStatus.SEALED:
            raise APIException("Only SEALED shipping notice can be uploaded")

        if notice.packages.count() == 0:
            raise APIException("No packages to make a template out of!")

        wb = make_cj_workbook(notice)

        filename = f"CJ_TEMPLATE_{notice.code}_{int(datetime.now().timestamp())}.xls"
        s3_path = f"cj-templates/{filename}"

        with default_storage.open(s3_path, 'wb') as f:
            wb.save(f)

        notice.template_url = f"https://alloff.s3.ap-northeast-2.amazonaws.com/{s3_path}"
        notice.save()

        return Response(
            ShippingNoticeSerializer(notice).data,
            status=status.HTTP_200_OK
        )

    @extend_schema(
        request=None,
        parameters=[OpenApiParameter("id", OpenApiTypes.STR, OpenApiParameter.PATH)],  # path variable was overridden
    )
    @action(detail=True, url_path="seal", methods=["POST"])
    def seal(self, request: Request, pk=None):
        notice = self.get_object()  # type: ShippingNotice
        if notice.status != ShippingNoticeStatus.LOCKED:
            raise APIException("Only LOCKED shipping notice can be sealed")

        if notice.packages.count() == 0:
            raise APIException("No packages to seal!")

        for package in notice.packages.all():
            seal_package(package)

        # Lock shipping notice so that additional inventories get a new shipping notice
        notice.status = ShippingNoticeStatus.SEALED
        notice.save()
        return Response(
            ShippingNoticeSerializer(notice).data,
            status=status.HTTP_200_OK
        )

    @extend_schema(
        request=None,
        parameters=[OpenApiParameter("id", OpenApiTypes.STR, OpenApiParameter.PATH)],  # path variable was overridden
    )
    @action(detail=True, url_path="package", methods=["POST"])
    def package(self, request: Request, pk=None):
        notice = self.get_object()  # type: ShippingNotice
        if notice.status != ShippingNoticeStatus.CREATED:
            raise APIException("Only CREATED shipping notice can be packaged")

        package_map = {}
        for item in notice.items.filter(package__isnull=True).all():
            order = item.item.extended_order.order
            payment = order.payment

            # Basic strategy --- bundle by orders
            if order.id not in package_map:
                package = Package.objects.create(
                    address=payment.buyeraddress,
                    postcode=payment.buyerpostcode,
                    recipient_name=payment.buyername,
                    recipient_mobile=payment.buyermobile,
                    notice=notice,
                )
                package_map[order.id] = package
                print(f"""Created package {package.code} for order {order.code}""")
            else:
                package = package_map[order.id]  # type: Package
            package.shipping_notice_items.add(item)
            print(f"""Added eoi {item.item.id} to package {package.code} for order {order.code}""")
            package.save()

        # Lock shipping notice so that additional inventories get a new shipping notice
        notice.status = ShippingNoticeStatus.LOCKED
        notice.save()
        return Response(
            self.get_serializer(notice).data,
            status=status.HTTP_200_OK
        )
