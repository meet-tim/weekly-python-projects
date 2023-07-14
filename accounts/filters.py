import django_filters
from django_filters import DateFilter,CharFilter
from .models import House

class HouseFilter(django_filters.FilterSet):
    #date_created = DateFilter(field_name="date_created", lookup_expr='gte')
    description = CharFilter(field_name="description", lookup_expr='icontains')
    
    price = CharFilter(field_name="price", lookup_expr='icontains')
    class Meta:
        model = House
        exclude = ('hitcount','exclusive','image1','image2','image3','image4','image5','available','date_created')