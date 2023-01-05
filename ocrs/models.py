from django.db import models
from django import forms

# Create your models here.


def uploaded_location(inst, f_name):
    return f"{inst.car_name}/{f_name}"


class Car(models.Model):
    image = models.ImageField(upload_to=uploaded_location,
                              null=True, blank=True,
                              width_field="width_field",
                              height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    car_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    num_of_seats = models.IntegerField()
    cost_per_day = models.CharField(max_length=50)
    content = models.TextField()
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.car_name

    def get_absolute_url(self):
        return f'/car/{self.id}'


class Order(models.Model):
    car_name = models.ForeignKey(Car, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=100)
    cell_no = models.CharField(max_length=20)
    address = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    closed = models.BooleanField(default=False)

    def __str__(self):
        return self.car_name.car_name

    def get_absolute_url(self):
        return f'/car/detail/{self.id}'

