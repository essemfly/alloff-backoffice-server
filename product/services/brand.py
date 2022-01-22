from alloff_backoffice_server.settings import PRODUCT_SERVER_URL
from office.services.base import GrpcService


class BrandService(generics.)
class BrandService(GrpcService):
    url = PRODUCT_SERVER_URL

    @classmethod
    def list(cls) -> List[dict]:
        request = 