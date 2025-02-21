from django.urls import path
from . import views
from .views import usersIndex

urlpatterns = [
    path("create", views.createUserView, name="createUserView"),
    path("createUser", views.createUser, name="createUser"),
    path("detail/<int:id>", views.userDetail, name="userDetail"),
    path("update/<int:id>", views.updateUser, name="updateUser"),
    path("createuser-by-fetch", views.createUserByFetch, name="createUserByFetch"),
    path('', usersIndex, name="users_index"),
]