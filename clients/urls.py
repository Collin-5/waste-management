from django.contrib import admin
from django.urls import path
from .views import client_list, add_clients

urlpatterns = [
    path("client_list/", client_list, name='clients'),
    path("client_add/", add_clients, name='add_clients'),
]
