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
from rest_framework import routers

# from office.viewsets.image import ImageUploaderViewSet
# from office.viewsets.admin_user import AdminUserViewSet
from office.viewsets.auth import (
    DecoratedTokenObtainPairView,
    DecoratedTokenRefreshView,
)
from office.viewsets.courier import CourierViewSet
from product.views.brand import BrandDetail, BrandList
from product.views.product import ProductDetail, ProductList
from product.views.product_group import ProductGroupDetail, ProductGroupList
from product.views.notification import NotificationDetail, NotificationList

# from office.viewsets.inventory import InventoryViewSet
# from tagger.viewsets.notification import NotificationViewSet
# from tagger.viewsets.order import OrderViewSet
# from tagger.viewsets.package import PackageViewSet
# from tagger.viewsets.received_items import ReceivedItemViewSet
# from tagger.viewsets.shipping_notice import ShippingNoticeViewSet, ShippingNoticeResultUploaderViewSet
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
# router.register(r"received-items", ReceivedItemViewSet, basename="received-items")
# router.register(r"inventories", InventoryViewSet, basename="inventories")
router.register(r"couriers", CourierViewSet, basename="couriers")
# router.register(r"admin-user", AdminUserViewSet, basename="admin-user")
# router.register(r"image-upload", ImageUploaderViewSet, basename="image-upload")
# router.register(r"shipping-notices", ShippingNoticeViewSet, basename="shipping-notices")
# router.register(r"shipping-notices-result-upload", ShippingNoticeResultUploaderViewSet, basename="shipping-notices-result-upload")
# router.register(r"packages", PackageViewSet, basename="packages")

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("brands/", BrandList.as_view()),
    path("brands/<str:brandID>/", BrandDetail.as_view()),
    path("timedeals/", ProductGroupList.as_view()),
    path("timedeals/<str:pgID>/", ProductGroupDetail.as_view()),
    path("notifications/", NotificationList.as_view()),
    path("notifications/<str:notiID>/", NotificationDetail.as_view()),
    path("products/", ProductList.as_view()),
    path("products/<str:productID>/", ProductDetail.as_view()),
    # path("token/", DecoratedTokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path("token/refresh/", DecoratedTokenRefreshView.as_view(), name="token_refresh"),
    # # YOUR PATTERNS
    # path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # # Optional UI:
    # path(
    #     "api/schema/swagger-ui/",
    #     SpectacularSwaggerView.as_view(url_name="schema"),
    #     name="swagger-ui",
    # ),
    # path(
    #     "api/schema/redoc/",
    #     SpectacularRedocView.as_view(url_name="schema"),
    #     name="redoc",
    # ),
]
