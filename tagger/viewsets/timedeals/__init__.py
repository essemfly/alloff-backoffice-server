from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets

from tagger.core.drf.search_filter import CustomSearchFilter
from tagger.core.mongo.models.alloff_product_group import AlloffProductGroup
from tagger.serializers.timedeal import TimedealSerializer


class TimedealViewSet(viewsets.ModelViewSet):
    queryset = AlloffProductGroup.objects().order_by("-id")
    filter_backends = [CustomSearchFilter]
    search_fields = [
        "title",
        "shorttitle"
    ]
    permission_classes = [IsAuthenticated]
    serializer_class = TimedealSerializer

    def destroy(self, request: Request, id=None):
        timedeal = self.get_object()  # type: AlloffProductGroup
        timedeal.hidden = True
        timedeal.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
