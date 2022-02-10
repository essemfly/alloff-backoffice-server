from rest_framework import serializers
from rest_framework.fields import IntegerField


class DeleteItemOrderMemoSerializer(serializers.Serializer):
    memo_id = IntegerField(required=True)
