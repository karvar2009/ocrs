from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('carlist/', views.car_list, name="car_list"),
    path('create_order/', views.create_order, name="create_order"),
    path('detail/<int:order_id>/', views.order_detail, name="order_detail"),
    path('<int:order_id>/delete_order/', views.order_delete, name="order_delete"),
    path('<str:brand>_<int:car_id>/', views.car_detail, name="car_detail"),
    path('<int:car_id>/edit/', views.car_edit, name="car_edit"),
    path('<int:car_id>/delete_car/', views.car_delete, name="car_delete"),
    path('newcar/', views.new_car, name="new_car"),
    path('contacts/', views.contacts, name="contacts"),
    path('popular_cars/', views.popular_cars, name="popular_cars"),
    path('<int:car_id>/like/', views.like_update, name="like")
]