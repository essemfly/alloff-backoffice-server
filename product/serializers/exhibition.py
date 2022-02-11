from rest_framework import serializers
from django_grpc_framework import proto_serializers
from product.serializers.product_group import ProductGroupSerializer
from protos.product.exhibition_pb2 import (
    CreateExhibitionRequest,
    EditExhibitionRequest,
    ExhibitionMessage,
    ListExhibitionsRequest,
    ListExhibitionsResponse,
)


class ExhibitionSerializer(proto_serializers.ProtoSerializer):
    exhibition_id = serializers.CharField()
    banner_image = serializers.CharField()
    thumbnail_image = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    start_time = serializers.DateTimeField()
    finish_time = serializers.DateTimeField()
    pgs = ProductGroupSerializer(many=True)

    class Meta:
        proto_class = ExhibitionMessage


class CreateExhibitionSerializer(proto_serializers.ProtoSerializer):
    banner_image = serializers.CharField()
    thumbnail_image = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    start_time = serializers.DateTimeField()
    finish_time = serializers.DateTimeField()
    pg_ids = serializers.ListField(serializers.CharField())

    class Meta:
        proto_class = CreateExhibitionRequest


class EditExhibitionSerializer(proto_serializers.ProtoSerializer):
    exhibition_id = serializers.CharField()
    banner_image = serializers.CharField(allow_null=True, required=False)
    thumbnail_image = serializers.CharField(allow_null=True, required=False)
    title = serializers.CharField(allow_null=True, required=False)
    description = serializers.CharField(allow_null=True, required=False)
    start_time = serializers.DateTimeField(allow_null=True, required=False)
    finish_time = serializers.DateTimeField(allow_null=True, required=False)
    pg_ids = serializers.ListField(
        serializers.CharField(), allow_null=True, required=False
    )

    class Meta:
        proto_class = EditExhibitionRequest


class ListExhibitionRequestSerializer(proto_serializers.ProtoSerializer):
    offset = serializers.IntegerField()
    limit = serializers.IntegerField()

    class Meta:
        proto_class = ListExhibitionsRequest


class ListExhibitionsResponseSerializer(proto_serializers.ProtoSerializer):
    exhibitions = ExhibitionSerializer(many=True)
    offset = serializers.IntegerField()
    limit = serializers.IntegerField()
    total_counts = serializers.IntegerField()

    class Meta:
        proto_class = ListExhibitionsResponse
