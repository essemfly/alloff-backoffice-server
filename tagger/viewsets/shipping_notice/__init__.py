from datetime import datetime

from django.core.files.storage import default_storage
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from tagger.core.label.print_label import print_label
from tagger.core.label.shipping_label import make_box_shipping_label, make_item_shipping_label
from tagger.models import ShippingNotice, Package
from tagger.models.inventory import InventoryStatus
from tagger.models.package import PackageStatus
from tagger.models.shipping_notice import ShippingNoticeStatus
from tagger.serializers.shipping import ShippingNoticeSerializer, PackageSerializer
from tagger.viewsets.shipping_notice.make_shipping_notice import make_shipping_notice
from tagger.viewsets.shipping_notice.template import make_cj_workbook


class ShippingNoticeViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = ShippingNotice.objects.order_by("-id")

    def list(self, request, *args, **kwargs):
        make_shipping_notice()
        return super().list(request, *args, **kwargs)

    serializer_class = ShippingNoticeSerializer

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
            items = package.shipping_notice_items.all()
            items_count = len(items)
            for index, item in enumerate(items):
                print(f"""MARKING SHIPPING PENDING - INV {item.inventory.code}""")
                item.inventory.status = InventoryStatus.SHIPPING_PENDING
                item.inventory.save()
                if items_count > 1:
                    print(f"""PRINTING ITEM LABEL FOR {package.code} ({package.recipient_name} {package.address})""")
                    print_label(make_item_shipping_label(package, item, index, items_count))

            print(f"""PRINTING BOX LABEL FOR {package.code} ({package.recipient_name} {package.address})""")
            print_label(make_box_shipping_label(package))
            package.status = PackageStatus.CREATED

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
            PackageSerializer(package_map.values(), many=True).data,
            status=status.HTTP_200_OK
        )
