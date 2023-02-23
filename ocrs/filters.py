import django_filters as df
from .models import Car
from django import forms


class CarFilter(df.FilterSet):
    class Meta:
        model = Car
        fields = ('company_name', 'num_of_seats',
                  'cost_per_day',)
        widgets = {
            'company_name': forms.Select(
                attrs={'class': 'form-select'}
            )
        }


