from django.urls import path, include
from transport.views import healthcheck

urlpatterns = [
    path("api/healthcheck/", healthcheck),
]
