from io import BytesIO
from os.path import splitext
from time import time

import shortuuid
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import InMemoryUploadedFile
from drf_spectacular.utils import extend_schema
from PIL import Image, ImageOps
from rest_framework import fields, parsers, response, serializers, status, viewsets
from rest_framework.decorators import action


class ImageUploaderRequestSerializer(serializers.Serializer):
    file = fields.FileField(required=True)
    path = fields.CharField(required=False)


class ImageUploaderResponseSerializer(serializers.Serializer):
    url = fields.URLField(required=True)
    origin_image_url = fields.URLField(required=False)
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
        origin_filename, file_extension = splitext(file.name)
        filename = f"{random_key}_{int(time())}_{origin_filename}{file_extension}"
        s3_folder = serializer.validated_data.get("path")
        if s3_folder == "" or s3_folder is None:
            s3_path = f"images/{filename}"
        else:
            s3_path = f"{s3_folder}/{filename}"

        with default_storage.open(s3_path, "wb") as f:
            for chunk in file.chunks():
                f.write(chunk)

        # upload webp if image
        if file_extension.lower() in [".png", ".jpg", ".jpeg", ".gif"]:
            webp_name = f"{random_key}_{int(time())}_{origin_filename}.webp"
            if s3_folder == "" or s3_folder is None:
                s3_webp_path = f"images/{webp_name}"
            else:
                s3_webp_path = f"{s3_folder}/{webp_name}"

            with default_storage.open(s3_webp_path, "wb") as f:
                webp = self.convert_to_webp(file)
                f.write(webp)

        else:
            s3_webp_path = s3_path

        serializer = ImageUploaderResponseSerializer(
            data={
                "random_key": random_key,
                "url": f"https://alloff.s3.ap-northeast-2.amazonaws.com/{s3_webp_path}",
                "origin_image_url": f"https://alloff.s3.ap-northeast-2.amazonaws.com/{s3_path}",
            }
        )

        return response.Response(
            serializer.initial_data,
            status=status.HTTP_200_OK,
        )

    def convert_to_webp(self, file):
        image = ImageOps.exif_transpose(Image.open(file))
        image_bytes = BytesIO()
        image.save(fp=image_bytes, format="WEBP")
        image_bytes = image_bytes.getvalue()
        return image_bytes
