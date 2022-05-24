from django_grpc_framework import proto_serializers
from gen.pyalloff.brand_pb2 import (
    BrandMessage,
    CreateBrandRequest,
    EditBrandRequest,
    SizeGuideMessage,
    InventoryMappingPolicyRequester,
    InventoryMappingPolicyMessage,
)
from rest_framework import serializers

from product.serializers.alloff_size import AlloffSizeSerializer


class SizeGuideSerializer(proto_serializers.ProtoSerializer):
    label = serializers.CharField(max_length=20)
    image_url = serializers.CharField()

    class Meta:
        proto_class = SizeGuideMessage


class InventoryMappingPolicyRequesterSerializer(proto_serializers.ProtoSerializer):
    brand_size = serializers.CharField()
    alloff_size_id = serializers.CharField()

    class Meta:
        proto_class = InventoryMappingPolicyRequester


class InventoryMappingPolicySerializer(proto_serializers.ProtoSerializer):
    brand_size = serializers.CharField()
    alloff_size = AlloffSizeSerializer()

    class Meta:
        proto_class = InventoryMappingPolicyMessage


class BrandSerializer(proto_serializers.ProtoSerializer):
    brand_id = serializers.CharField(max_length=100)
    keyname = serializers.CharField(max_length=50)
    korname = serializers.CharField(max_length=50)
    engname = serializers.CharField(max_length=50)
    logo_image_url = serializers.CharField()
    description = serializers.CharField(max_length=50)
    is_popular = serializers.BooleanField(default=False)
    is_open = serializers.BooleanField(default=True)
    is_hide = serializers.BooleanField(default=False)
    in_maintenance = serializers.BooleanField(default=False)
    size_guide = SizeGuideSerializer(many=True)
    back_image_url = serializers.CharField()
    inventory_mapping_policies = InventoryMappingPolicySerializer(many=True)

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
    is_hide = serializers.BooleanField(default=False)
    size_guide = SizeGuideSerializer(many=True)
    back_image_url = serializers.CharField()
    inventory_mapping_policies = InventoryMappingPolicyRequesterSerializer(many=True)

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
    is_hide = serializers.BooleanField(default=False, allow_null=True, required=False)
    size_guide = SizeGuideSerializer(many=True, allow_null=True, required=False)
    back_image_url = serializers.CharField(allow_null=True, required=False)
    inventory_mapping_policies = InventoryMappingPolicyRequesterSerializer(allow_null=True, required=False, many=True)

    class Meta:
        proto_class = EditBrandRequest
