from rest_framework import serializers
from django_grpc_framework import proto_serializers

from logistics.models import Package, PackageStatus
from logistics.protos.package_proto import package_pb2


class PackageProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Package
        proto_class = package_pb2.Package
        fields = "__all__"


class PackageSerializer(serializers.Serializer):
    key = serializers.UUIDField()

    status = serializers.ChoiceField(choices=PackageStatus.choices)
    related_order_item_ids = serializers.ListField(
        child=serializers.CharField(max_length=20)
    )

    # destination address
    customer_name = serializers.CharField(max_length=20)
    customer_contact = serializers.CharField(max_length=13)
    base_address = serializers.CharField(max_length=255)
    detail_address = serializers.CharField(
        max_length=50, allow_null=True, allow_blank=True
    )
    postal_code = serializers.CharField(max_length=6)
    delivery_note = serializers.CharField(
        max_length=50, allow_null=True, allow_blank=True
    )

    # tracking info
    tracking_number = serializers.CharField(
        max_length=50, allow_null=True, allow_blank=True
    )
    # tracking_courier = serializers.ForeignKey(
    #     Courier,
    #     on_delete=serializers.DO_NOTHING,
    #     null=True,
    #     blank=True,
    # )

    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    deleted_at = serializers.DateTimeField()
