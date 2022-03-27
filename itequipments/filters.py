import django_filters
from .models import All_equipment
from django_filters import CharFilter


class EquipmentFilter(django_filters.FilterSet):
    asset_no = CharFilter(field_name="asset_no", lookup_expr='icontains')

    class Meta:
        model = All_equipment
        fields = ['asset_no']