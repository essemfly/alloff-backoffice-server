

from tagger.core.pushserver.base import BasePushNotification


class ProductDiffPush(BasePushNotification):
    NAVIGATE_TO = "/products"

    def __init__(self, reference_id=""):
        super().__init__(reference_id=reference_id)
