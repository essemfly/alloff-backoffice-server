from typing import Optional, Tuple

from alloff_backoffice_server.settings import COMPANY_API_HEADER
from django.http.request import HttpRequest
from office.models.api import ApiKey, ApiKeyStatus
from office.models.company import CompanyStatus
from office.serializers.order_item import *
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied


def with_company_api(original_func):
    def wrapper_func(self, request, *args, **kwargs):
        new_request, _ = _set_request_user(request)
        return original_func(self, new_request, *args, **kwargs)

    wrapper_func.__name__ = original_func.__name__
    return wrapper_func


def _set_request_user(request: HttpRequest) -> Tuple[HttpRequest, ApiKey]:
    api_key = _get_api_key(request)
    if api_key is None:
        return request, None
    request._force_auth_user = api_key.api_user
    request.user = api_key.api_user
    return request, api_key


def _get_api_key(request: HttpRequest) -> Optional[ApiKey]:
    try:
        api_key_value: str = request.headers[COMPANY_API_HEADER]
        api_key = ApiKey.objects.get(key=api_key_value)
        if api_key.status != ApiKeyStatus.ACTIVE:
            raise PermissionDenied("Api key is inactive")
        elif api_key.company.status != CompanyStatus.ACTIVE:
            raise PermissionDenied("Company is inactive")
        return api_key
    except KeyError:
        return None
    except ApiKey.DoesNotExist:
        raise AuthenticationFailed("Invalid API key")
