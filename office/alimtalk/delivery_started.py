from tagger.core.alimtalk.base import BaseAlimtalk


class DeliveryStartedAlimtalk(BaseAlimtalk):
    TEMPLATE_CODE = "deliveryStartedTrack"

    def add(
        self,
        mobile: str = None,
        grouping_key: str = None,
        productName: str = None,
        trackingNumber: str = None,
    ) -> "BaseAlimtalk":
        data = {"productName": productName, "trackingNumber": trackingNumber}
        return self._add(
            mobile=mobile,
            data=data,
            grouping_key=grouping_key,
        )
