from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Tuple
from alloff_backoffice_server.settings import ALIMTALK
from office.alimtalk.client import AlimtalkClient


class BaseAlimtalk(ABC):
    def __init__(self, grouping_key: str) -> None:
        self.__client = AlimtalkClient()
        self.sender_grouping_key = grouping_key
        self.recipients = []  # type: List[Tuple[str, str, Dict]]
        super().__init__()

    @property
    @abstractmethod
    def TEMPLATE_CODE(self) -> str:
        pass

    @abstractmethod
    def add(self, mobile: str = None, grouping_key: str = None) -> "BaseAlimtalk":
        pass

    def _add(
        self, mobile: str = None, grouping_key: str = None, data: Dict = None
    ) -> "BaseAlimtalk":
        self.recipients.append((mobile, grouping_key, data))
        return self

    @property
    def recipient_list(self) -> List[Dict]:
        return [
            {
                "templateParameter": data,
                "recipientNo": mobile,
                "recipientGroupingKey": grouping_key,
            }
            for (mobile, grouping_key, data) in self.recipients
        ]

    def send(self) -> Optional[str]:
        data = {
            "senderKey": ALIMTALK.get("SENDER_KEY"),
            "templateCode": self.TEMPLATE_CODE,
            "recipientList": self.recipient_list,
            "senderGroupingKey": self.sender_grouping_key,
        }
        res = self.__client.send(data)

        success = res.get("header").get("isSuccessful")

        if not success:
            print(res, data)
            return None

        return res.get("message").get("requestId")
