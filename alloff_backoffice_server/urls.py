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
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework import routers

from tagger.viewsets.admin_user import AdminUserViewSet
from tagger.viewsets.auth import (
    DecoratedTokenObtainPairView,
    DecoratedTokenRefreshView,
)
from tagger.viewsets.brands import BrandViewSet
from tagger.viewsets.notification import NotificationViewSet
from tagger.viewsets.image import ImageUploaderViewSet
from tagger.viewsets.order import OrderViewSet
from tagger.viewsets.timedeal_product_templates import TimedealProductTemplateViewSet
from tagger.viewsets.timedeal_products import TimedealProductViewSet
from tagger.viewsets.timedeals import TimedealViewSet


router = routers.DefaultRouter()
router.register(r"orders", OrderViewSet, basename="orders")
router.register(r"timedeals", TimedealViewSet, basename="timedeals")
router.register(r"timedeal-products", TimedealProductViewSet, basename="timedeal-products")
router.register(r"timedeal-product-templates", TimedealProductTemplateViewSet, basename="timedeal-product-templates")
router.register(r"notifications", NotificationViewSet, basename="notifications")
router.register(r"admin-user", AdminUserViewSet, basename="admin-user")
router.register(r"image-upload", ImageUploaderViewSet, basename="image-upload")
router.register(r"brands", BrandViewSet, basename="brands")

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("token/", DecoratedTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", DecoratedTokenRefreshView.as_view(), name="token_refresh"),
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
