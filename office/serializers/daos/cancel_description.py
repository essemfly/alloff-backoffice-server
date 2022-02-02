from rest_framework import serializers


class CancelDescriptionDAOSerializer(serializers.Serializer):
    RefundAvailable = serializers.BooleanField()
    ChangeAvailable = serializers.BooleanField()
    ChangeFee = serializers.IntegerField()
    RefundFee = serializers.IntegerField()
