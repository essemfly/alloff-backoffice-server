import pandas as pd
from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema
from rest_framework import fields, parsers, serializers, status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from office.serializers.shipping_notice import ShippingNoticeSerializer

class ExcelUploaderRequestSerializer(serializers.Serializer):
    file = fields.FileField(required=True)
    notice_id = fields.CharField(required=True)


class ShippingNoticeResultUploaderViewSet(viewsets.GenericViewSet):
    serializer_class = ExcelUploaderRequestSerializer
    parser_classes = [
        parsers.MultiPartParser,
        parsers.FormParser,
        parsers.FileUploadParser,
    ]

    @extend_schema(responses={status.HTTP_200_OK: ShippingNoticeSerializer})
    @action(methods=["POST"], detail=False)
    def upload(self, request):
        serializer = self.get_serializer(
            data=request.data
        )  # type: ImageUploaderRequestSerializer
        serializer.is_valid(raise_exception=True)

        file = serializer.validated_data.get("file")  # type: InMemoryUploadedFile
        notice_id = serializer.validated_data.get(
            "notice_id"
        )  # type: InMemoryUploadedFile
        notice = ShippingNotice.objects.filter(id=notice_id).first()

        if notice is None:
            raise APIException(f"No shipping notice found with id {notice_id}")
        if notice.status != ShippingNoticeStatus.SEALED:
            raise APIException("Only SEALED shipping notice can be shipped")

        courier = Courier.objects.filter(name="CJ대한통운").first()
        if courier is None:
            raise APIException("Courier not found")

        try:
            df = pd.read_html(file, match="주소", header=0)[0]
        except ValueError:
            raise APIException("Malformed Excel!")

        df = df.dropna(subset=["주문번호", "상태"]).astype(str)
        if {row["주문번호"] for _, row in df.iterrows()} != {
            x.code for x in notice.packages.all()
        }:
            raise APIException("Package codes do not match!")

        for _, row in df.iterrows():
            tracking_number = row["송장번호"]
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
                    "delivery_tracking_number": package.courier.name
                    + " "
                    + package.tracking_number,
                    "delivery_tracking_url": package.tracking_url,
                }
                s = ChangeStatusSerializer(data=status_change_data, instance=order)
                s.is_valid(raise_exception=True)
                _change_status(
                    s,
                    order,
                    User.objects.get(username="backoffice_server"),
                    id=str(order.id),
                )
                print(
                    "-----------------------------------------------------------------------"
                )
                print(
                    f"""[{package.code}] {package.recipient_name} ({package.recipient_mobile})"""
                )
                for item in package.shipping_notice_items.all():
                    print(
                        f"ㄴ https://office.alloff.co/orders/{item.item.extended_order.order.code}"
                    )
                    print(f"""   [INV {item.inventory.code}] {item.item.name}""")
                    item.inventory.status = InventoryStatus.SHIPPED
                    item.inventory.save()

        notice.status = ShippingNoticeStatus.SHIPPED
        notice.save()

        return Response(
            ShippingNoticeSerializer(notice).data, status=status.HTTP_200_OK
        )
