from django.db import models
from drf_spectacular.utils import extend_schema_serializer
from numpy import require
from rest_framework import serializers
from django_grpc_framework import proto_serializers
from product.serializers.product_group import ProductGroupSerializer
from gen.pyalloff.exhibition_pb2 import (
    CreateExhibitionRequest,
    EditExhibitionRequest,
    ExhibitionMessage,
    ListExhibitionsRequest,
    ListExhibitionsResponse,
    ExhibitionType,
)



class ExhibitionSerializer(proto_serializers.ProtoSerializer):
    exhibition_id = serializers.CharField()
    banner_image = serializers.CharField()
    thumbnail_image = serializers.CharField()
    title = serializers.CharField()
    subtitle = serializers.CharField()
    description = serializers.CharField()
    start_time = serializers.DateTimeField()
    finish_time = serializers.DateTimeField()
    pgs = ProductGroupSerializer(many=True)
    is_live = serializers.BooleanField()
    exhibition_type = serializers.ChoiceField(choices=ExhibitionType.items())
    target_sales = serializers.IntegerField()
    current_sales = serializers.IntegerField()

    class Meta:
        proto_class = ExhibitionMessage


class CreateExhibitionSerializer(proto_serializers.ProtoSerializer):
    banner_image = serializers.CharField()
    thumbnail_image = serializers.CharField()
    title = serializers.CharField()
    subtitle = serializers.CharField()
    description = serializers.CharField()
    start_time = serializers.DateTimeField()
    finish_time = serializers.DateTimeField()
    pg_ids = serializers.ListField(
        child=serializers.CharField(), allow_null=True, required=False
    )
    exhibition_type = serializers.ChoiceField(choices=ExhibitionType.items())
    target_sales = serializers.IntegerField()

    class Meta:
        proto_class = CreateExhibitionRequest


class EditExhibitionSerializer(proto_serializers.ProtoSerializer):
    exhibition_id = serializers.CharField()
    banner_image = serializers.CharField(allow_null=True, required=False)
    thumbnail_image = serializers.CharField(allow_null=True, required=False)
    title = serializers.CharField(allow_null=True, required=False)
    subtitle = serializers.CharField(allow_null=True, required=False)
    description = serializers.CharField(allow_null=True, required=False)
    start_time = serializers.DateTimeField(allow_null=True, required=False)
    finish_time = serializers.DateTimeField(allow_null=True, required=False)
    pg_ids = serializers.ListField(
        child=serializers.CharField(), allow_null=True, required=False
    )
    is_live = serializers.BooleanField(allow_null=True, required=False)
    target_sales = serializers.IntegerField(allow_null=True, required=False)

    class Meta:
        proto_class = EditExhibitionRequest


class ListExhibitionRequestSerializer(proto_serializers.ProtoSerializer):
    offset = serializers.IntegerField(allow_null=True, required=False)
    limit = serializers.IntegerField(allow_null=True, required=False)
    exhibition_type = serializers.ChoiceField(choices=ExhibitionType.items())
    is_live = serializers.BooleanField()
    query = serializers.CharField(max_length=30, allow_null=True, required=False)

    class Meta:
        proto_class = ListExhibitionsRequest


@extend_schema_serializer(many=False)
class ListExhibitionsResponseSerializer(proto_serializers.ProtoSerializer):
    exhibitions = ExhibitionSerializer(many=True)
    offset = serializers.IntegerField()
    limit = serializers.IntegerField()
    total_counts = serializers.IntegerField()
    group_type = serializers.ChoiceField(choices=ExhibitionType.items())
    is_live = serializers.BooleanField()
    query = serializers.CharField()

    class Meta:
        proto_class = ListExhibitionsResponse
