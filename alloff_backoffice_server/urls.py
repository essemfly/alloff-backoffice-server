"""alloff_backoffice_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers
from tagger.views import test
from tagger.viewsets.admin_user import AdminUserViewSet
from tagger.viewsets.auth import (
    DecoratedLogoutView,
    DecoratedTokenObtainPairView,
    DecoratedTokenRefreshView,
)
from tagger.viewsets.order import OrderViewSet

router = routers.DefaultRouter()
router.register(r"orders", OrderViewSet, basename="orders")
router.register(r"admin-user", AdminUserViewSet, basename="admin-user")

schema_view = get_schema_view(
    openapi.Info(
        title="Alloff Backoffice API",
        default_version="v1",
        description="API for backoffice",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    # path("api-auth/", include("rest_framework.urls")),
    path("token/", DecoratedTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", DecoratedTokenRefreshView.as_view(), name="token_refresh"),
    path("token/logout/", DecoratedLogoutView.as_view(), name="token_logout"),
    path("test/", test),
    url(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    url(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    url(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]
