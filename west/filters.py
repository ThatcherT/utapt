import django_filters

from .models import *

class ApartmentFilter(django_filters.FilterSet):
    address = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Apartment
        fields = {
        'price': ['lt', 'gt'],
        'area' : ['exact'],
        'name':['icontains']
        }
