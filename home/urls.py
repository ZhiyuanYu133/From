# -*-coding:utf-8 -*-

from django.urls import path, re_path

from .views import *

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

    # user follow
    path('add_follow/<int:id>', add_follow, name="add_follow"),
    path('user_follows/', get_user_follows, name="user_follows"),
    path('get_user_friends/', get_user_friends, name="get_user_friends"),
    path('add_friends/<int:id>', add_friends, name="add_friends"),
    path('get_user_inbox/', get_user_inbox, name="user_inbox"),
    path('update_inbux_state/<int:id>', update_inbux_state, name="update_inbux_state"),
    path('delete_friends/<int:id>', delete_friends, name="delete_friends"),
    path('get_all_users/', get_all_users, name="get_all_users"),
    path('read/<int:id>', read, name="read"),

]

app_name = "home"
