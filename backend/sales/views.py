from .filters import SaleFilter
from .pagination import CustomPagination
from .models import Sale
from .serializers import SaleSerializer
from rest_framework import viewsets, mixins 
from django_filters import rest_framework as filters


# Create your views here.
class SaleViewset(
  mixins.ListModelMixin, 
  viewsets.GenericViewSet
):
  queryset = Sale.objects.all()
  serializer_class = SaleSerializer
  pagination_class = CustomPagination
  filter_backends = (filters.DjangoFilterBackend,)
  filterset_class = SaleFilter

