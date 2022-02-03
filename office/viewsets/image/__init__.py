from time import time

import shortuuid
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework import (fields, parsers, response, serializers, status,
                            viewsets)
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema


class ImageUploaderRequestSerializer(serializers.Serializer):
    file = fields.FileField(required=True)
    path = fields.CharField(required=False)


class ImageUploaderResponseSerializer(serializers.Serializer):
    url = fields.URLField(required=True)
    random_key = fields.CharField(required=True)


class ImageUploaderViewSet(viewsets.GenericViewSet):
    serializer_class = ImageUploaderRequestSerializer
    parser_classes = [
        parsers.MultiPartParser,
        parsers.FormParser,
        parsers.FileUploadParser,
    ]

    @extend_schema(responses={status.HTTP_200_OK: ImageUploaderResponseSerializer})
    @action(methods=["POST"], detail=False)
    def upload(self, request):
        serializer = self.get_serializer(
            data=request.data
        )  # type: ImageUploaderRequestSerializer
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data.get("file")  # type: InMemoryUploadedFile
        random_key = shortuuid.random(length=6)
        filename = f"{random_key}_{int(time())}_{file.name}"
        s3_folder = serializer.validated_data.get("path")
        if s3_folder == "":
            s3_path = f"images/{filename}"
        else:
            s3_path = f"{s3_folder}/{filename}"

        with default_storage.open(s3_path, "wb") as f:
            for chunk in file.chunks():
                f.write(chunk)
        return response.Response(
            ImageUploaderResponseSerializer(
                data={
                    "random_key": random_key,
                    "url": f"https://alloff.s3.ap-northeast-2.amazonaws.com/{s3_path}",
                }
            ).initial_data,
            status=status.HTTP_200_OK,
        )