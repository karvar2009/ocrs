from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from .models import Car, Order, Brands, Specifications, FeedbackMsg
from django.db import models
# Register your models here.


class CarAdmin(admin.ModelAdmin):
    list_display = ("car_name", "cost_per_day", "image", "booked",)
    list_editable = ("cost_per_day", "booked",)
    list_filter = ("cost_per_day",)
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple}
    }


class OrderAdmin(admin.ModelAdmin):
    list_display = ("car_name", "start_date", "end_date", "closed", "employee_name",)
    list_editable = ("end_date", "closed",)
    list_filter = ("employee_name", "closed", "car_name",)


class BrandAdmin(admin.ModelAdmin):
    list_display = ("brand_name", "segment",)
    list_filter = ("segment",)


class SpecificationsAdmin(admin.ModelAdmin):
    list_display = ('name',)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'check',)
    list_filter = ('checked',)


admin.site.register(Specifications, SpecificationsAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Brands, BrandAdmin)
admin.site.register(FeedbackMsg, FeedbackAdmin)
