from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q  # работа с поисковыми запросами в Django
from django.contrib.auth.decorators import login_required
from .models import Car, Order, FeedbackMsg, Brands
from .filters import CarFilter
from .forms import CarForm, FeedbackForm, OrderForm
from slider.models import Slider
from datetime import datetime
# Create your views here.


def home(request):
    now = datetime.now()
    slider_data = Slider.objects.filter(active_from__lte=now, active_to__gte=now).order_by('position')
    return render(request, "home.html", {'title': "Car rental | Minsk", 'slider': slider_data})


def car_list(request):
    cars = Car.objects.order_by('like').order_by('-booked')
    query = request.GET.get('q')  # забираем запрос от формы с методом отправки GET
    brand = request.GET.get('brand')
    model = request.GET.get('model')
    price_lower = request.GET.get('price_lower')
    price_upper = request.GET.get('price_upper')
    if query:  # если запрос состоялся
        cars = cars.filter(
            Q(car_name__icontains=model),
            Q(company_name__icontains=brand),
            Q(cost_per_day__ltd=price_upper)
        )
    # пагинация
    paginator = Paginator(cars, 10)  # отображаем по 5 машин на странице
    page = request.GET.get('page')
    try:
        cars = paginator.page(page)
    except PageNotAnInteger:  # если пользователь вписал номер страницы как текст
        cars = paginator.page(1)  # перенесем его на первую страницу с машинами
    except EmptyPage:  # если пользователь вписал номер страницы, например, 9999999
        cars = paginator.page(paginator.num_pages)  # перемещаем его на последнюю страницу с машинами
    return render(request, "car_list.html", {'title': 'Список автомобилей', 'cars': cars, 'filter': query})


@login_required
def create_order(request, car_id=None):
    car = get_object_or_404(Car, pk=car_id)
    form = OrderForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.car_name = car
        delta = datetime.date(instance.end_date) - datetime.date(instance.start_date)
        instance.price = delta.days * int(instance.car_name.cost_per_day)
        instance.save()
        car.booked = True
        car.save()
        return redirect('order_detail')
    return render(request, "create_order.html", {"title": "Create order"})


@login_required
def order_detail(request, order_id=None):
    order = get_object_or_404(Order, id=order_id)
    return render(request, "order_detail.html", {"order": order})


def order_update(request, order_id=None):
    query = get_object_or_404(Car, order_id=order_id)
    form = CarForm(request.POST or None, instance=query)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())


def order_delete(request, order_id=None):
    query = get_object_or_404(Order, order_id=order_id)
    query.delete()
    return redirect('home')


def car_detail(request, name=None):
    car = get_object_or_404(Car, name=name)
    return render(request, "car_details.html", {"car": car, 'title': 'Изменение автомобиля'})


def car_edit(request, car_id=None):
    query = get_object_or_404(Car, id=car_id)
    form = CarForm(request.POST or None, instance=query)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    return render(request, "car_edit.html", {"title": "Update car info"})


def car_delete(request, car_id=None):
    query = get_object_or_404(Car, car_id=car_id)
    query.delete()
    cars = Car.objects.all()
    return render(request, "admin_index.html", {"cars": cars})


def new_car(request):
    new = Car.objects.order_by('-id')
    query = request.GET.get('q')
    if query:  # если запрос состоялся
        new = new.filter(
            Q(car_name__icontains=query),
            Q(company_name__icontains=query),
            Q(cost_per_day__icontains=query),
            Q(num_of_seats__icontains=query)
        )
        paginator = Paginator(new, 12)
        page = request.GET.get('page')
        try:
            new = paginator.page(page)
        except PageNotAnInteger:
            new = paginator.page(1)
        except EmptyPage:
            new = paginator.page(paginator.num_pages)
    return render(request, "new_car.html", {"car": new})


def contacts(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('contacts')
    return render(request, "contacts.html",  {"title": "Contact with us", 'form': form})


def like_update(request, car_id=None):
    like_count = get_object_or_404(Car, id=car_id)
    like_count.like += 1
    like_count.save()
    return redirect('car_list')
