import pandas as pd
from django.core.files.uploadedfile import InMemoryUploadedFile
from drf_spectacular.utils import extend_schema
from office.serializers.shipping_notice import ShippingNoticeSerializer
from office.viewsets.image import ImageUploaderRequestSerializer
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

    @extend_schema(responses={status.HTTP_200_OK: ShippingNoticeSerializer})
    @action(methods=["POST"], detail=False)
    def upload(self, request):
        serializer = self.get_serializer(
            data=request.data
        )  # type: ImageUploaderRequestSerializer
        serializer.is_valid(raise_exception=True)

        file = serializer.validated_data.get("file")  # type: InMemoryUploadedFile
        notice_id = serializer.validated_data.get("notice_id")  # type: int

        try:
            df = pd.read_html(file, match="주소", header=0)[0]
        except ValueError:
            raise APIException("Malformed Excel!")

        df = df.dropna(subset=["주문번호", "상태"]).astype(str)

        return Response({"message": "ok"}, status=status.HTTP_200_OK)
