from django.urls import path, include
from .views import SaleViewset

from rest_framework import routers


router = routers.DefaultRouter()
router.register('sales', SaleViewset, basename='sales')

urlpatterns = [
    path('', include(router.urls)),
]