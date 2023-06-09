from django.contrib import admin

from .models import User, UserFollow, UserFriends, UserInbux

admin.site.site_header = 'CMPUT404Project'
admin.site.site_title = 'CMPUT404Project'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "uuid", "username", "displayName", "gender", "email", "host"]


@admin.register(UserFollow)
class DoctorsAdmin(admin.ModelAdmin):
    list_display = ["create_user", "follow_to", "follow_time", "is_followed", "hosts", "follow_to_hosts"]


@admin.register(UserFriends)
class UserFriendsAdmin(admin.ModelAdmin):
    list_display = ["id", "create_user_name", "friend_to_username", "is_agreed", "friend_time", "hosts",
                    "friend_to_hosts"]


@admin.register(UserInbux)
class UserInbuxAdmin(admin.ModelAdmin):
    list_display = ["create_username", "operator_username", "action", "url", "detail", "add_time", "is_read"]
