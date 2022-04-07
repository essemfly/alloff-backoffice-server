from grpc import RpcError, StatusCode
from rest_framework.exceptions import APIException, NotFound


def grpc_exception(original_func):
    def wrapper_func(self, *args, **kwargs):
        try:
            return original_func(self, *args, **kwargs)
        except RpcError as e:
            exception_kwargs = {
                "detail": e.details(),
                "code": e.code(),
            }
            exception = NotFound if e.code() == StatusCode.NOT_FOUND else APIException
            raise exception(**exception_kwargs)

    wrapper_func.__name__ = original_func.__name__
    return wrapper_func
