from django.urls import path
from . import views
from .views import usersIndex

urlpatterns = [
    path('', usersIndex, name="users_index"),
]