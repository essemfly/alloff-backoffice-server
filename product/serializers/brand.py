from rest_framework import serializers
from django_grpc_framework import proto_serializers
from protos.product.brand_pb2 import (
    BrandMessage,
    CreateBrandRequest,
    EditBrandRequest,
    SizeGuideMessage,
)


class SizeGuideSerializer(proto_serializers.ProtoSerializer):
    label = serializers.CharField(max_length=20)
    image_url = serializers.CharField()

    class Meta:
        proto_class = SizeGuideMessage


class BrandSerializer(proto_serializers.ProtoSerializer):
    brand_id = serializers.CharField(max_length=100)
    keyname = serializers.CharField(max_length=50)
    korname = serializers.CharField(max_length=50)
    engname = serializers.CharField(max_length=50)
    logo_image_url = serializers.CharField()
    description = serializers.CharField(max_length=50)
    is_popular = serializers.BooleanField(default=False)
    is_open = serializers.BooleanField(default=True)
    in_maintenance = serializers.BooleanField(default=False)
    size_guide = SizeGuideSerializer(many=True)
    back_image_url = serializers.CharField()

    class Meta:
        proto_class = BrandMessage


class CreateBrandSerializer(proto_serializers.ProtoSerializer):
    keyname = serializers.CharField(max_length=50)
    korname = serializers.CharField(max_length=50)
    engname = serializers.CharField(max_length=50)
    logo_image_url = serializers.CharField()
    description = serializers.CharField(max_length=50)
    is_popular = serializers.BooleanField(default=False)
    is_open = serializers.BooleanField(default=True)
    in_maintenance = serializers.BooleanField(default=False)
    size_guide = SizeGuideSerializer(many=True)
    back_image_url = serializers.CharField()

    class Meta:
        proto_class = CreateBrandRequest


class EditBrandSerializer(proto_serializers.ProtoSerializer):
    keyname = serializers.CharField(max_length=50)
    korname = serializers.CharField(max_length=50, allow_null=True, required=False)
    engname = serializers.CharField(max_length=50, allow_null=True, required=False)
    logo_image_url = serializers.CharField(allow_null=True, required=False)
    description = serializers.CharField(max_length=50, allow_null=True, required=False)
    is_popular = serializers.BooleanField(
        default=False, allow_null=True, required=False
    )
    is_open = serializers.BooleanField(default=True, allow_null=True, required=False)
    in_maintenance = serializers.BooleanField(
        default=False, allow_null=True, required=False
    )
    size_guide = SizeGuideSerializer(many=True, allow_null=True, required=False)
    back_image_url = serializers.CharField(
        max_length=50, allow_null=True, required=False
    )

    class Meta:
        proto_class = EditBrandRequest
