from typing import Optional, Tuple

from alloff_backoffice_server.settings import COMPANY_API_HEADER
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.http.request import HttpRequest
from office.models.api import ApiKey, ApiKeyStatus
from office.models.company import CompanyStatus
from rest_framework.exceptions import APIException


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request: HttpRequest):
        try:
        # Code to be executed for each request before
            # the view (and later middleware) are called.
            request, _ = self._set_request_user(request)
            response = self.get_response(request)

            # Code to be executed for each request/response after
            # the view is called.

            return response
        except APIException as e:
            return HttpResponseForbidden(e.detail)

    def _set_request_user(self, request: HttpRequest) -> Tuple[HttpRequest, ApiKey]:
        api_key = self._get_api_key(request)
        if api_key is None:
            return request, None
        request._force_auth_user = api_key.api_user
        return request, api_key

    def _get_api_key(self, request: HttpRequest) -> Optional[ApiKey]:
        try:
            api_key_value: str = request.headers[COMPANY_API_HEADER]
            api_key = ApiKey.objects.get(key=api_key_value)
            if api_key.status != ApiKeyStatus.ACTIVE:
                raise APIException("Api key is inactive")
            elif api_key.company.status != CompanyStatus.ACTIVE:
                raise APIException("Company is inactive")
            return api_key
        except KeyError:
            return None
        except ApiKey.DoesNotExist:
            raise APIException("Invalid API key")
