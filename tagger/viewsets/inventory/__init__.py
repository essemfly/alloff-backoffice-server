from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets

from tagger.models.inventory import Inventory


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects
    permission_classes = [IsAuthenticated]
