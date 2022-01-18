from datetime import datetime
from tagger.core.alimtalk.base import BaseAlimtalk
import arrow


class CancelFinishedAlimtalk(BaseAlimtalk):
    TEMPLATE_CODE = "paymentCanceled"

    def add(
        self,
        mobile: str = None,
        grouping_key: str = None,
        productName: str = None,
        amount: int = None,
    ) -> "BaseAlimtalk":
        data = {
            "상품명": productName,
            "결제금액": str(amount),
            "취소시간": arrow.now("Asia/Seoul").format("YYYY-MM-DD HH:mm:ss"),
        }
        return self._add(
            mobile=mobile,
            data=data,
            grouping_key=grouping_key,
        )
