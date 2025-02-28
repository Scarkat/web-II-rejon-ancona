from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Evento, Localidad, Producto, Boleto

def examenIndex(request):
    evento = Evento.objects.all()
    return render(request, "examen/index.html", {"evento":evento})

def examenEvento(request):
    evento = Evento.objects.all()
    return render(request, "examen/eventos.html", {"evento":evento})

def examenBoleto(request):
    boleto = Boleto.objects.all()
    return render(request, "examen/boletos.html", {"boleto":boleto})