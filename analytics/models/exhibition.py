from dataclasses import dataclass
from datetime import datetime
from typing import Optional

import arrow
from django.contrib.auth.models import User
from gen.pyalloff.exhibition_pb2 import GetExhibitionRequest
from office.services.order_item import OrderItemService
from product.services.exhibition import ExhibitionService

GROUP_TYPES = {
    0: "NORMAL",
    1: "TIMEDEAL",
    2: "GROUPDEAL",
}


@dataclass
class ExhibitionCVR:
    exhibition_id: str = ""
    exhibition_title: str = ""
    start_time: str = ""
    finish_time: str = ""
    live_hours: int = -1
    exhibition_type: str = ""
    num_products: int = -1
    num_payments: int = -1
    is_unique_users: bool = True

    __detail = None

    @staticmethod
    def make(exhibition_id: str, is_unique_users=True) -> "ExhibitionCVR":
        record = ExhibitionCVR(
            exhibition_id=exhibition_id,
            is_unique_users=is_unique_users,
        )
        return record.init()

    def init(self) -> "ExhibitionCVR":
        return self.__feed_detail().__feed_num_payments().__feed_live_hours()

    @property
    def parsed_start_time(self) -> Optional[datetime]:
        if self.start_time is None or self.start_time == "":
            return None
        return self._parse_datetime(self.start_time)

    @property
    def parsed_finish_time(self) -> Optional[datetime]:
        if self.finish_time is None or self.finish_time == "":
            return None
        return self._parse_datetime(self.finish_time)

    @property
    def detail(self):
        if self.__detail is not None:
            return self.__detail

        get_req = GetExhibitionRequest(exhibition_id=self.exhibition_id)
        self.__detail = ExhibitionService.get(get_req)
        return self.__detail

    def __feed_num_payments(self) -> "ExhibitionCVR":
        order_items_res = self.__get_order_items_response()
        items = order_items_res.results
        user_item_hashmap = {item.order.user["id"]: 0 for item in items}
        if self.is_unique_users:
            self.num_payments = len(user_item_hashmap)
        else:
            self.num_payments = len(items)
        return self

    def __feed_live_hours(self) -> "ExhibitionCVR":
        if self.parsed_start_time is None:
            self.live_hours = 0
            return self

        finish_time = (
            self.parsed_finish_time
            if self.parsed_finish_time is not None
            else datetime.now()
        )

        secs = (finish_time - self.parsed_start_time).total_seconds()
        self.live_hours = secs / 60 / 60
        return self

    def __feed_detail(self) -> "ExhibitionCVR":
        num_products = 0
        for pg in self.detail.pgs:
            num_products += len(pg.products)
        self.num_products = num_products

        self.exhibition_title = self.detail.title
        self.start_time = self.detail.start_time
        self.finish_time = self.detail.finish_time

        self.exhibition_type = GROUP_TYPES[self.detail.exhibition_type]
        return self

    def __get_order_items_response(self):
        user = User.objects.get(username="admin")
        return OrderItemService.List(
            user=user, page=1, size=10000, exhibition_id=self.exhibition_id
        )

    @staticmethod
    def _parse_datetime(dt: str) -> datetime:
        return datetime.strptime(dt.split("+")[0], "%Y-%m-%d %H:%M:%S ")

    @property
    def google_sheet_row(self):
        num_weekends = 0
        for r in arrow.Arrow.range(
            "day", self.parsed_start_time, self.parsed_finish_time
        ):
            if r.weekday() in [5, 6]:
                num_weekends += 1
        return [
            self.exhibition_id,  # ID
            self.exhibition_title,  # 제목
            self.exhibition_type,  # 타입
            self.parsed_start_time.isoformat(),  # 시작 시간
            self.parsed_finish_time.isoformat(),  # 마감 시간
            self.live_hours,  # 진행시간(h)
            num_weekends,  # 주말일수
            self.num_products,  # 상품갯수
            self.num_payments,  # 결제
        ]
