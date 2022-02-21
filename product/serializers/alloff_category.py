from drf_spectacular.utils import extend_schema_serializer
from django.db import models
from django_grpc_framework import proto_serializers
from drf_spectacular.utils import extend_schema_serializer
from protos.product.alloffcategory_pb2 import (AlloffCategoryMessage,
                                               ListAlloffCategoryRequest)
from rest_framework import serializers


class AlloffCategorySerializer(proto_serializers.ProtoSerializer):
    category_id = serializers.CharField()
    name = serializers.CharField()
    keyname = serializers.CharField()
    level = serializers.IntegerField()
    parent_id = serializers.CharField()
    img_url = serializers.CharField()

    class Meta:
        proto_class = AlloffCategoryMessage


class ListAlloffCateogoryRequestSerializer(proto_serializers.ProtoSerializer):
    parent_id = serializers.CharField(allow_null=True, required=False)

    class Meta:
        proto_class = ListAlloffCategoryRequest


@extend_schema_serializer(many=False)
class ListAlloffCategoryResponseSerializer(proto_serializers.ProtoSerializer):
    categories = AlloffCategorySerializer(many=True)
