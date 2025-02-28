from django.urls import path
from . import views
from .views import examenIndex

urlpatterns = [
    path("boletos", views.examenBoleto, name="examen_boleto"),
    path("eventos", views.examenEvento, name="examen_evento"),
    path("", examenIndex, name="examen_index"),
]