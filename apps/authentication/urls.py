# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user, add_user, users_list
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('users/', users_list, name="users"),
    path('add_user/', add_user, name="add_users"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout")
]
