from typing import List

from iamport import Iamport


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


class _Singleton:
    __instance = None

    @classmethod
    def __get_instance(cls):
        return cls.__instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.instance = cls.__get_instance
        return cls.__instance


class IMP(_Singleton):
    __iamport: Iamport = None

    def __init__(self):
        self.__iamport = self.__get_iamport()

    def __get_iamport(self):
        return Iamport(
            imp_key="8089061252601456",
            imp_secret="oR8RlO2aSV7Uzj86wK8FbGl8ZPeTmscLjlCEaFP2AXWag5gNPos15N94CoXZRaKavnPF3EIECFOTK4GA",
        )

    def cancel_payment(self, uid: str, amount: int, checksum: int, reason: str):
        res = self.__iamport.cancel_by_imp_uid(
            uid, reason, amount=amount, checksum=None
        )
        return res

    def get_payment_details(self, uids: List[str]):
        split_uids = chunks(uids, 100)  # Per Iamport REST API spec
        result = []
        for uids in split_uids:
            formatted_params = ["imp_uid[]=" + uid for uid in uids]
            res = self.__iamport.find_by_imp_uid("?" + "&".join(formatted_params))
            result += res
        return result

    def get_payment_detail(self, uid: str):
        try:
            return self.__iamport.find_by_merchant_uid(uid)
        except:
            return None
