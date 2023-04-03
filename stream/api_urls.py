# -*-coding:utf-8 -*-

from django.urls import path

from . import api_views

urlpatterns = [
    path('posts/<int:pk>', api_views.PostsView.as_view()),
    path('create_post/', api_views.create_post),
    # path('<int:pk>/', api_views.APIDetail.as_view()),
]
