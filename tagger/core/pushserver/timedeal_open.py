

from tagger.core.pushserver.base import BasePushNotification


class TimedealOpenPush(BasePushNotification):
    NAVIGATE_TO = "/timedeals"

    def __init__(self, reference_id=""):
        super().__init__(reference_id=reference_id)
