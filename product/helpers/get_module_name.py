from django.contrib.auth.models import User
from office.models.company import CompanyStatus
from rest_framework.exceptions import NotAuthenticated, PermissionDenied


def get_module_name(request) -> str:
    user: User = request.user
    if user.is_anonymous:
        raise NotAuthenticated("User is not authenticated.")
    elif user.profile.is_admin:
        # Empty string will be treated as None by grpc
        return ""
    elif (
        user.profile.company is None
        or user.profile.company.status != CompanyStatus.ACTIVE
    ):
        raise PermissionDenied("User is not in an active company.")

    return user.profile.company.name
