from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CompanyViewSet, MaterialListingViewSet, health

router = DefaultRouter()
router.register(r"companies", CompanyViewSet, basename="companies")
router.register(r"material-listings", MaterialListingViewSet, basename="material-listings")

urlpatterns = [
    path("health/", health),
    path("", include(router.urls)),
]
