from django.urls import path, include
from rest_framework.routers import DefaultRouter

from transport.views import VehicleViewSet, DriverViewSet, OrderViewSet

router = DefaultRouter()
router.register(r"vehicles", VehicleViewSet)
router.register(r"drivers", DriverViewSet)
router.register(r"orders", OrderViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]