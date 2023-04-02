#-*-coding:utf-8 -*-

from django.urls import path, include, re_path
from .views import *
from django.contrib import admin


urlpatterns = [
    path('get_auth_posts/', get_auth_posts, name="get_auth_posts"),
    path('add_auth_posts/', add_auth_posts, name="add_auth_posts"),
    path('add_comment/', add_comment, name="add_comment"),
    path('add_like_history/', add_like_history, name="add_like_history"),
    path('get_post_detail/<int:pk>', get_post_detail, name="get_post_detail"),
]

app_name = "stream"


