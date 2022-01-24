from rest_framework import serializers
from django_grpc_framework import proto_serializers
from protos.product.brand_pb2 import BrandMessage, SizeGuideMessage


class SizeGuideSerializer(proto_serializers.ProtoSerializer):
    label = serializers.CharField(max_length=20)
    image_url = serializers.URLField()

    class Meta:
        proto_class = SizeGuideMessage


class BrandSerializer(proto_serializers.ProtoSerializer):
    brand_id = serializers.CharField(max_length=100)
    keyname = serializers.CharField(max_length=50)
    korname = serializers.CharField(max_length=50)
    engname = serializers.CharField(max_length=50)
    logo_image_url = serializers.URLField()
    description = serializers.CharField(max_length=300)
    is_popular = serializers.BooleanField(default=False)
    is_open = serializers.BooleanField(default=True)
    in_maintenance = serializers.BooleanField(default=False)
    size_guide = SizeGuideSerializer(many=True)

    class Meta:
        proto_class = BrandMessage
