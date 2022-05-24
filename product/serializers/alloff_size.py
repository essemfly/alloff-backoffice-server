from django_grpc_framework import proto_serializers
from drf_spectacular.utils import extend_schema_serializer
from product.serializers.alloff_category import AlloffCategorySerializer
from rest_framework import serializers
from gen.pyalloff.alloff_size_pb2 import (
    AlloffSizeMessage,
    ListAlloffSizeRequest,
    ListAlloffSizeResponse,
    EditAlloffSizeRequest,
    CreateAlloffSizeRequest,
    GetAlloffSizeRequest,
)


class AlloffSizeSerializer(proto_serializers.ProtoSerializer):
    alloff_size_id = serializers.CharField()
    alloff_size_name = serializers.CharField()
    original_size_name = serializers.CharField()
    alloff_category = AlloffCategorySerializer()

    class Meta:
        proto_class = AlloffSizeMessage


class ListAlloffSizeRequestSerializer(proto_serializers.ProtoSerializer):

    class Meta:
        proto_class = ListAlloffSizeRequest


@extend_schema_serializer(many=False)
class ListAlloffSizeReponseSerializer(proto_serializers.ProtoSerializer):
    alloff_sizes = AlloffSizeSerializer(many=True)

    class Meta:
        proto_class = ListAlloffSizeResponse


class CreateAlloffSizeSerializer(proto_serializers.ProtoSerializer):
    alloff_size_name = serializers.CharField()
    original_size_name = serializers.CharField()
    alloff_category_id = serializers.CharField()

    class Meta:
        proto_class = CreateAlloffSizeRequest


class EditAlloffSizeSerializer(proto_serializers.ProtoSerializer):
    alloff_size_id = serializers.CharField()
    alloff_size_name = serializers.CharField(allow_null=True, allow_blank=True, required=False)
    original_size_name = serializers.CharField(allow_null=True, allow_blank=True, required=False)
    alloff_category_id = serializers.CharField(allow_null=True, allow_blank=True, required=False)

    class Meta:
        proto_class = EditAlloffSizeRequest


class GetAlloffSizeSerializer(proto_serializers.ProtoSerializer):
    alloff_size_id = serializers.CharField()

    class Meta:
        proto_class = GetAlloffSizeRequest
