from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Tuple
from alloff_backoffice_server.settings import ALIMTALK
from tagger.core.pushserver.client import PushServerClient


class BasePushNotification(ABC):
    __client = PushServerClient()

    def __init__(self, reference_id=""):
        self.reference_id = reference_id
        super().__init__()

    @property
    @abstractmethod
    def NAVIGATE_TO(self):
        pass

    def send(self, title, message, devices):
        data = {
            "notifications": [{
                "tokens": devices,
                "platform": 2,
                "title": title,
                "message": message,
                "data": {
                    "type": "navigation",
                    "navigateTo": self.__client.navigate_url + self.NAVIGATE_TO + self.reference_id
                }
            }]
        }
        res = self.__client.send(data)
        return res
