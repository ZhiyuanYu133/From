# -*-coding:utf-8 -*-

from django.urls import path

from . import api_views

urlpatterns = [
    path('', api_views.APIList.as_view()),
    path('<int:pk>/', api_views.APIDetail.as_view()),
]
