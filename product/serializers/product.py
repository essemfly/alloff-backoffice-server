from rest_framework import serializers
from django_grpc_framework import proto_serializers
from product.protos import product_pb2

class PersonProtoSerializer(proto_serializers.ProtoSerializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)

    class Meta:
        proto_class = product_pb2.ProductMessage