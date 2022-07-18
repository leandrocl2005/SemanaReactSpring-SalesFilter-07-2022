from django_filters import rest_framework as filters
from .models import Sale


class SaleFilter(filters.FilterSet):
    seller_name = filters.CharFilter(field_name="seller_name", lookup_expr="iexact")
    date = filters.DateFromToRangeFilter(field_name='date')

    class Meta:
        model = Sale
        fields = ['seller_name', 'date']

# http://localhost:8000/api/sales/?seller_name=logan&date_before=2021-12-31&date_after=2021-12-01