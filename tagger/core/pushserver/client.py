from alloff_backoffice_server.settings import PUSHSERVER
import httpx
import simplejson


class PushServerClient:
    @property
    def url(self):
        return PUSHSERVER.get("URL")

    @property
    def navigate_url(self):
        return PUSHSERVER.get("NAVIGATE_URL")

    @property
    def headers(self) -> str:
        return {
            "Content-Type": "application/json",
        }

    def send(self, data: dict):
        res = httpx.post(
            url=self.url, headers=self.headers, data=simplejson.dumps(data)
        )
        return res.json()
