from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def indexOrders(request):
    return HttpResponse("Hello, world. You're at the orders index.")