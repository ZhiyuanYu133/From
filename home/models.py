import uuid

from django.db import models
from django.utils import timezone



class User(models.Model):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "User"

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(max_length=32, unique=True, verbose_name="username")  # unique
    password = models.CharField(max_length=32, verbose_name="password")
    displayName = models.CharField(max_length=100, blank=True, null=True)
    gender = models.BooleanField(default=1, verbose_name="gender")
    phone = models.CharField(max_length=32, blank=True, null=True, unique=True, verbose_name="phone")
    email = models.EmailField(blank=True, null=True, unique=True, verbose_name="email")
    address = models.TextField(blank=True, null=True, verbose_name="address")
    host = models.CharField(max_length=100, default='localhost:8000/')
    url = models.CharField(max_length=100, blank=True)
    github = models.CharField(max_length=100, blank=True, null=True)
    profileImage = models.ImageField(default="profile_pics/happy-face.png", upload_to="profile_pics", blank=True)
    is_active = models.BooleanField(default=0, verbose_name="can login")
    is_delete = models.BooleanField(default=0, verbose_name="is delete")
    create_time = models.DateTimeField(auto_created=True, default=timezone.now)

    def __str__(self):
        return self.username


# UserFollow
class UserFollow(models.Model):
    create_user = models.CharField(max_length=256)
    create_user_name = models.CharField(max_length=256)
    follow_to = models.CharField(max_length=256)
    follow_time = models.DateTimeField(auto_now_add=True)
    is_followed = models.BooleanField(default=0)
    hosts = models.TextField(default="")
    follow_to_hosts = models.TextField(default="")


class UserFriends(models.Model):
    create_user = models.CharField(max_length=256)
    create_user_name = models.CharField(max_length=256)
    friend_to = models.CharField(max_length=256)
    friend_to_username = models.CharField(max_length=256)
    is_agreed = models.BooleanField(default=0)
    friend_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    hosts = models.TextField(default="")
    friend_to_hosts = models.TextField(default="")
