from drf_spectacular.utils import extend_schema_serializer
from django.db import models
from rest_framework import serializers
from django_grpc_framework import proto_serializers

from protos.product.alloffcategory_pb2 import (
    AlloffCategoryMessage,
    ListAlloffCategoryRequest,
)


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
    parent_id = serializers.CharField()

    class Meta:
        proto_class = ListAlloffCategoryRequest


class ListAlloffCategoryResponseSerializer(proto_serializers.ProtoSerializer):
    categories = AlloffCategorySerializer(many=True)
