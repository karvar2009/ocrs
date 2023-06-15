from django import forms
from .models import Car, Order, FeedbackMsg
from tinymce.widgets import TinyMCE


class CarForm(forms.ModelForm):
    class Meta:
        model = Car   # модель, на основе которой строится форма
        fields = [
            "image",
            "car_name",
            "company_name",
            "num_of_seats",
            "cost_per_day",
            "content",
        ]  # поля для формы
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'company_name': forms.Select(attrs={'class': 'form-select form control'}),
            'num_of_seats': forms.NumberInput(attrs={'class': 'form-control'}),
            'cost_per_day': forms.NumberInput(attrs={'class': 'form-control'}),
            'content': TinyMCE(attrs={'cols': 100, 'rows': 20})
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'address',
            'start_date',
            'end_date',
        ]
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackMsg
        exclude = ('checked',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'content': TinyMCE(attrs={'cols': 100, 'rows': 20})
        }


