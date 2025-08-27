from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from transport.views import VehicleViewSet, DriverViewSet, OrderViewSet

from transport.views import VehicleViewSet, DriverViewSet, OrderViewSet

router = DefaultRouter()
router.register(r"vehicles", VehicleViewSet)
router.register(r"drivers", DriverViewSet)
router.register(r"orders", OrderViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
]