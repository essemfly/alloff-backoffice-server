from rest_framework import serializers


class UserDAOSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    uuid = serializers.CharField()
    mobile = serializers.CharField()
    email = serializers.CharField()
    baseaddress = serializers.CharField()
    detailaddress = serializers.CharField()
    postcode = serializers.CharField()
    created_at = serializers.DateTimeField()
