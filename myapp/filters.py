from django_filters import filterset, filters
from myapp.models import Ad


class AdFilter(filterset.FilterSet):
    price__gt = filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = filters.NumberFilter(field_name='price', lookup_expr='lt')
    rooms__gt = filters.NumberFilter(field_name='rooms', lookup_expr='gt')
    rooms__lt = filters.NumberFilter(field_name='rooms', lookup_expr='lt')

    class Meta:
        model = Ad
        fields = ['price', 'state', 'city', 'rooms', 'type']