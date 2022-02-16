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
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from office.viewsets.admin_user import AdminUserViewSet

from office.viewsets.image import ImageUploaderViewSet
from office.viewsets.auth import DecoratedTokenObtainPairView, DecoratedTokenRefreshView
from office.viewsets.shipping_notice_uploader import ShippingNoticeResultUploaderViewSet

# from office.viewsets.courier import CourierViewSet
from product.viewsets.product_group import ProductGroupViewSet
from product.viewsets.product import ProductViewSet
from product.viewsets.brand import BrandViewSet
from product.viewsets.notification import NotificationViewSet
from product.viewsets.exhibition import ExhibitionViewSet
from product.viewsets.hometab import HometabItemViewSet
from product.viewsets.top_banner import TopBannerViewSet
from office.viewsets.inventory import InventoryViewSet
from office.viewsets.order_items import OrderItemViewSet

from office.viewsets.package import PackageViewSet
from office.viewsets.received_item import ReceivedItemViewSet

from office.viewsets.shipping_notice import ShippingNoticeViewSet
from rest_framework import routers

from protos.product.exhibition_pb2_grpc import Exhibition

# from tagger.viewsets.notification import NotificationViewSet
# from tagger.viewsets.order import OrderViewSet
# from tagger.viewsets.package import PackageViewSet
# from tagger.viewsets.received_items import ReceivedItemViewSet
# from office.viewsets.shipping_notice import (
#     ShippingNoticeViewSet,
# )

# from tagger.viewsets.timedeal_product_templates import TimedealProductTemplateViewSet
# from tagger.viewsets.timedeal_products import TimedealProductViewSet
# from tagger.viewsets.timedeals import TimedealViewSet

router = routers.DefaultRouter()
# router.register(r"orders", OrderViewSet, basename="orders")
# router.register(r"timedeals", TimedealViewSet, basename="timedeals")
# router.register(
#     r"timedeal-products", TimedealProductViewSet, basename="timedeal-products"
# )
# router.register(
#     r"timedeal-product-templates",
#     TimedealProductTemplateViewSet,
#     basename="timedeal-product-templates",
# )

router.register(r"notifications", NotificationViewSet, basename="notifications")
router.register(r"order-items", OrderItemViewSet, basename="order-items")
router.register(r"received-items", ReceivedItemViewSet, basename="received-items")
router.register(r"inventories", InventoryViewSet, basename="inventories")
# router.register(r"couriers", CourierViewSet, basename="couriers")
router.register(r"packages", PackageViewSet, basename="packages")
router.register(r"shipping-notices", ShippingNoticeViewSet, basename="shipping-notices")
router.register(r"admin-user", AdminUserViewSet, basename="admin-user")
router.register(r"brands", BrandViewSet, basename="brands")
router.register(r"products", ProductViewSet, basename="products")
router.register(r"product-groups", ProductGroupViewSet, basename="product-groups")
router.register(r"exhibitions", ExhibitionViewSet, basename="exhibitions")
router.register(r"hometabs", HometabItemViewSet, basename="hometabs")
router.register(r"notifications", NotificationViewSet, basename="notifiactions")
router.register(r"top-banners", TopBannerViewSet, basename="top-banner")
router.register(r"image-upload", ImageUploaderViewSet, basename="image-upload")
router.register(
    r"shipping-notices-result-upload",
    ShippingNoticeResultUploaderViewSet,
    basename="shipping-notices-result-upload",
)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("token/", DecoratedTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", DecoratedTokenRefreshView.as_view(), name="token_refresh"),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
