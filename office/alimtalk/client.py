from alloff_backoffice_server.settings import ALIMTALK
import httpx
import simplejson


class AlimtalkClient:
    @property
    def url(self) -> str:
        return ALIMTALK.get("URL").format(ALIMTALK.get("APP_KEY"))

    @property
    def headers(self) -> str:
        return {
            "Content-Type": "application/json",
            "X-Secret-Key": ALIMTALK.get("SECRET"),
        }

    def send(self, data: dict):
        res = httpx.post(
            url=self.url, headers=self.headers, data=simplejson.dumps(data)
        )
        return res.json()
