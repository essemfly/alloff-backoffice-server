from django.core.files.uploadedfile import InMemoryUploadedFile
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets, parsers, serializers, fields, response, status
from rest_framework.decorators import action
from django.core.files.storage import default_storage
import shortuuid
from time import time


class ImageUploaderRequestSerializer(serializers.Serializer):
    file = fields.FileField(required=True)


class ImageUploaderResponseSerializer(serializers.Serializer):
    url = fields.URLField(required=True)
    random_key = fields.CharField(required=True)


class ImageUploaderViewSet(viewsets.GenericViewSet):
    serializer_class = ImageUploaderRequestSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser, parsers.FileUploadParser, ]

    @extend_schema(
        responses={status.HTTP_200_OK: ImageUploaderResponseSerializer}
    )
    @action(methods=["POST"], detail=False)
    def upload(self, request):
        serializer = self.get_serializer(data=request.data)  # type: ImageUploaderRequestSerializer
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data.get("file")  # type: InMemoryUploadedFile
        random_key = shortuuid.random(length=6)
        filename = f"{random_key}_{int(time())}_{file.name}"
        s3_path = f"images/{filename}"
        with default_storage.open(s3_path, 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)
        return response.Response(
            ImageUploaderResponseSerializer(data={
                "random_key": random_key,
                "url": f"https://alloff.s3.ap-northeast-2.amazonaws.com/{s3_path}"
            }).initial_data,
            status=status.HTTP_200_OK)
