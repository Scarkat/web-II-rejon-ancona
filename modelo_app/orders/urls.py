from django.urls import path

from . import views

urlpatterns = [
    path('', views.indexOrders, name="orders_index"),
]