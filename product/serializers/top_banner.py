from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers
from django_grpc_framework import proto_serializers
from gen.python.protos.topbanner_pb2 import (
    CreateTopBannerRequest,
    EditTopBannerRequest,
    ListTopBannersRequest,
    ListTopBannersResponse,
    TopBannerMessage,
)


class TopBannerSerializer(proto_serializers.ProtoSerializer):
    banner_id = serializers.CharField()
    banner_image = serializers.CharField()
    exhibition_id = serializers.CharField()
    title = serializers.CharField()
    subtitle = serializers.CharField()
    is_live = serializers.BooleanField()
    weight = serializers.IntegerField()

    class Meta:
        proto_class = TopBannerMessage


class CreateTopBannerSerializer(proto_serializers.ProtoSerializer):
    banner_image = serializers.CharField()
    exhibition_id = serializers.CharField()
    title = serializers.CharField()
    subtitle = serializers.CharField()
    is_live = serializers.BooleanField()
    weight = serializers.IntegerField()

    class Meta:
        proto_class = CreateTopBannerRequest


class EditTopBannerSerializer(proto_serializers.ProtoSerializer):
    banner_id = serializers.CharField()
    banner_image = serializers.CharField(allow_null=True, required=False)
    exhibition_id = serializers.CharField(allow_null=True, required=False)
    title = serializers.CharField(allow_null=True, required=False)
    subtitle = serializers.CharField(allow_null=True, required=False)
    is_live = serializers.BooleanField(allow_null=True, required=False)
    weight = serializers.IntegerField(allow_null=True, required=False)

    class Meta:
        proto_class = EditTopBannerRequest


class ListTopBannerRequestSerializer(proto_serializers.ProtoSerializer):
    offset = serializers.IntegerField(allow_null=True, required=False)
    limit = serializers.IntegerField(allow_null=True, required=False)

    class Meta:
        proto_class = ListTopBannersRequest


@extend_schema_serializer(many=False)
class ListTopBannerResponseSerializer(proto_serializers.ProtoSerializer):
    banners = TopBannerSerializer(many=True)
    offset = serializers.IntegerField()
    limit = serializers.IntegerField()
    total_counts = serializers.IntegerField()

    class Meta:
        proto_class = ListTopBannersResponse
