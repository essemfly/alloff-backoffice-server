from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Tuple
from alloff_backoffice_server.settings import ALIMTALK
from tagger.core.pushserver.client import PushServerClient


class BasePushNotification(ABC):
    __client = PushServerClient()
    prod_test_devices = [
        "c0IfW-xzdUx3nu6XmpzXNz:APA91bGYmuaoWsdoNzhp_SqUiaKm_8bPK-MfUgmJpmvprUui6run4qKTEeF8QpPSnrR7f5oK2Suy5BJduO04C2DuKWmYHbYZJCRy_FtI6Rm6kAxEopwiRSGjymiqGzXVpz8i8nffFYV1",
        "dJ4rSV2L60aLpHxQjxoFz-:APA91bGJR2YXQkmBbv0rELM6caPUeZ3C1MnBkz1wlI68wCzDRhc9Bsma3stSCRXTGip-6mxdtj2GfuMT4c0XV85AWDuLr0lkH33VDNRsuc8nqo24JGOHmDDpYl_wetLh9vYL-3I0A6ID",
        "cBRNxXqZwEeapVVni8KJcG:APA91bG7UnRCfxWvNR7ngSYNfhTazApx9yAlQXtXqCJDWpn_X-cwVMnnUDLmjLUCso9s7_oiP_xrBkOqoa-1ie3LaRsckENluZTaxWcNAKpdUvVZtV9Pq_TRgRdmwtpA0kE_-Mx-_Nzl",
        "eEx9IUeGQtGgo__aVsJih4:APA91bG0NaGdVP_2NyfBWAXXXdZ0-iR9J-pRTf6JxjueMowaIg9HQDYiZ5PkGeqTypblQNDg-Fecdask8W6o15lNHOhzCHfHzIzofE63APEZPNQQbRVjaaBCTk6m3kAeIqoBuJl9rmHh",
    ]

    def __init__(self, reference_id=""):
        self.reference_id = reference_id
        super().__init__()

    @property
    @abstractmethod
    def NAVIGATE_TO(self):
        pass

    def send(self, title, message, devices, is_test=True):
        print("URL?", self.__client.navigate_url + self.NAVIGATE_TO + self.reference_id)
        data = {
            "notifications": [{
                "tokens": self.prod_test_devices if is_test else devices,
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
