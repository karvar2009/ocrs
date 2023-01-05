from django.shortcuts import render
from .models import Car
# Create your views here.


def home(request):
    car = Car.objects.all()
    context = {
        "title": "Car rental list",
        "cars": car,
    }
    return render(request, "car_list.html", {'cars': car})
