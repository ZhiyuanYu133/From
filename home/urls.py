#-*-coding:utf-8 -*-

from django.urls import path, include, re_path
from .views import *
from django.contrib import admin


urlpatterns = [
    re_path('^$', index),
    path('index/', index),
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),

    # profile
    path('user_info/', user_info, name="user_info"),
    path('change_userinfo/', change_userinfo, name="change_userinfo"),
    path('change_password/', change_password, name="change_password"),
    path('forget_password/', forget_password, name="forget_password"),
    path('send_code/', send_code, name="send_code"),

    # post info详情
    path('doctors_detail/', doctors_detail, name="doctors_detail"),
    path('type_messages/', type_messages, name="type_messages"),
    path('doctors_messages/', doctors_messages, name="doctors_messages"),
]

app_name = "home"


