from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)
from office.viewsets.admin_user import AdminUserViewSet
from office.viewsets.auth import (DecoratedTokenObtainPairView,
                                  DecoratedTokenRefreshView)
from office.viewsets.courier import CourierViewSet
from office.viewsets.image import ImageUploaderViewSet
from office.viewsets.auth import DecoratedTokenObtainPairView, DecoratedTokenRefreshView
from office.viewsets.shipping_notice_uploader import ShippingNoticeResultUploaderViewSet
from product.viewsets.product_group import ProductGroupViewSet
from product.viewsets.product import ProductViewSet
from product.viewsets.brand import BrandViewSet
from product.viewsets.notification import NotificationViewSet
from product.viewsets.exhibition import ExhibitionViewSet
from product.viewsets.hometab import HometabItemViewSet
from product.viewsets.top_banner import TopBannerViewSet
from office.viewsets.inventory import InventoryViewSet
from office.viewsets.order_items import OrderItemBackofficeViewSet
from office.viewsets.order_items.api import OrderItemCompanyApiViewSet
from office.viewsets.package import PackageViewSet
from office.viewsets.product_inquiry import ProductInquiryViewSet
from office.viewsets.received_item import ReceivedItemViewSet
from office.viewsets.shipping_notice import ShippingNoticeViewSet
from office.viewsets.shipping_notice_uploader import \
    ShippingNoticeResultUploaderViewSet
from product.viewsets.alloff_category import AlloffCategoryViewSet
from product.viewsets.brand import BrandViewSet
from product.viewsets.exhibition import ExhibitionViewSet
from product.viewsets.hometab import HometabItemViewSet
from product.viewsets.notification import NotificationViewSet
from product.viewsets.product import ProductViewSet
from product.viewsets.product_group import ProductGroupViewSet
from rest_framework import routers

from alloff_backoffice_server.settings import API_TYPE_IS_COMPANY_API
from protos.product.exhibition_pb2_grpc import Exhibition
router = routers.DefaultRouter()

if API_TYPE_IS_COMPANY_API:
    router.register(
        r"order-items",
        OrderItemCompanyApiViewSet,
        basename="order-items",
    )
else:
    router.register(r"order-items", OrderItemBackofficeViewSet, basename="order-items")
    router.register(r"received-items", ReceivedItemViewSet, basename="received-items")
    router.register(r"inventories", InventoryViewSet, basename="inventories")
    router.register(r"packages", PackageViewSet, basename="packages")
    router.register(
        r"shipping-notices", ShippingNoticeViewSet, basename="shipping-notices"
    )
    router.register(r"admin-user", AdminUserViewSet, basename="admin-user")
    router.register(r"product-groups", ProductGroupViewSet, basename="product-groups")
    router.register(r"exhibitions", ExhibitionViewSet, basename="exhibitions")
    router.register(r"hometabs", HometabItemViewSet, basename="hometabs")
    router.register(r"top-banners", HometabItemViewSet, basename="top-banner")
    router.register(r"notifications", NotificationViewSet, basename="notifiactions")

    router.register(
        r"shipping-notices-result-upload",
        ShippingNoticeResultUploaderViewSet,
        basename="shipping-notices-result-upload",
    )
    router.register(r"image-upload", ImageUploaderViewSet, basename="image-upload")
    router.register(
        r"shipping-notices-result-upload",
        ShippingNoticeResultUploaderViewSet,
        basename="shipping-notices-result-upload",
    )

router.register(r"alloff-categories", AlloffCategoryViewSet, basename="alloff-category")
router.register(r"brands", BrandViewSet, basename="brands")
router.register(r"couriers", CourierViewSet, basename="couriers")
router.register(r"products", ProductViewSet, basename="products")

router.register(r"inquiries", ProductInquiryViewSet, basename="inquiries")

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
