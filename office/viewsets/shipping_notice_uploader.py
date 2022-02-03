from typing import List

import pandas as pd
from drf_spectacular.utils import extend_schema
from office.serializers.shipping_notice import (
    ShippingNoticeListSerializer,
    ShippingNoticeRetrieveSerializer,
    ShippingNoticeStatus,
)
from office.services.shipping_notice import PackageTrackingPair, ShippingNoticeService
from rest_framework import fields, parsers, serializers, status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.response import Response


class ExcelUploaderRequestSerializer(serializers.Serializer):
    file = fields.FileField(required=True)
    notice_id = fields.IntegerField(required=True)


class ShippingNoticeResultUploaderViewSet(viewsets.GenericViewSet):
    serializer_class = ExcelUploaderRequestSerializer
    parser_classes = [
        parsers.MultiPartParser,
        parsers.FormParser,
        parsers.FileUploadParser,
    ]

    @extend_schema(
        request=ExcelUploaderRequestSerializer,
        responses=ShippingNoticeRetrieveSerializer,
    )
    @action(methods=["POST"], detail=False)
    def upload(self, request):
        serializer = ExcelUploaderRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        file = serializer.validated_data.get("file")
        notice_id = serializer.validated_data.get("notice_id")

        notice = ShippingNoticeService.retrieve(id=notice_id)

        if notice is None:
            raise APIException(f"No shipping notice found with id {notice_id}")
        if notice.status == ShippingNoticeStatus.SHIPPED:
            raise APIException("Shipped notices cannot be altered!")

        try:
            df = pd.read_html(file, match="주소", header=0)[0]
        except ValueError:
            pass
        
        try:
            df = pd.read_excel(file)
        except Exception:
            raise APIException("Malformed Excel!")

        df = df.dropna(subset=["주문번호", "상태"]).astype(str)

        pairs: List[PackageTrackingPair] = [
            {"package_code": row["주문번호"], "tracking_number": row["송장번호"]}
            for (_, row) in df.iterrows()
        ]

        notice = ShippingNoticeService.submit_tracking_excel(
            id=notice_id,
            tracking_pairs=pairs,
            user=request.user,
        )

        return Response(
            ShippingNoticeListSerializer(notice).data, status=status.HTTP_200_OK
        )
