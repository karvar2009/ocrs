from django.shortcuts import render, get_object_or_404
from .models import Car, Order
# Create your views here.


def home(request):
    return render(request, "home.html", {'title': "Car rental | Minsk"})


def car_list(request):
    cars = Car.objects.all()
    return render(request, "car_list.html", {'cars': cars})


def create_order(request):
    return render(request, "create_order.html", {"title": "Create order"})


def order_detail(request, order_id=None):
    detail = get_object_or_404(Order, order_id=order_id)
    return render(request, "order_detail.html", {"detail": detail})


def order_delete(request, order_id=None):
    query = get_object_or_404(Order, order_id=order_id)
    query.delete()
    return ''


def car_detail(request, brand, car_id=None):
    detail = get_object_or_404(Car, car_id=car_id)
    return render(request, "car_detail.html", {"detail": detail})


def car_edit(request, car_id=None):
    query = get_object_or_404(Car, car_id=car_id)
    # TODO: здесь форма изменения машины
    return render(request, "car_edit.html", {"title": "Update car info"})


def car_delete(request, car_id=None):
    query = get_object_or_404(Car, car_id=car_id)
    query.delete()
    cars = Car.objects.all()
    return render(request, "admin_index.html", {"cars": cars})


def new_car(request):
    new = Car.objects.order_by('-id')
    return render(request, "new_car.html", {"car": new})


def contacts(request):
    return render(request, "contacts.html",  {"title": "Contact with us"})


def like_update(request, car_id=None):
    new = Car.objects.order_by('-id')
    like_count = get_object_or_404(Car, car_id=car_id)
    like_count.like += 1
    like_count.save()
    return render(request, "new_car.html", {"car": new})


def popular_cars(request):
    popular = Car.objects.order_by('-like')
    return render(request, "popular_cars.html", {"popular": popular})
