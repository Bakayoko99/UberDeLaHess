from django.urls import path
from . import views
from rideRequest import views
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('user', views.UserList.as_view())
]
