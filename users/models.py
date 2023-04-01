import uuid

from PIL import Image
from django.contrib.auth.models import User
from django.db import models


# AuthUser
class AuthUser(models.Model):
    # In API
    username = models.CharField(max_length=100, verbose_name="username")
    password = models.CharField(max_length=30, verbose_name="password")
    email = models.EmailField(default="", verbose_name="email")
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    host = models.CharField(max_length=100, default='localhost:8000/')
    displayName = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True)
    github = models.CharField(max_length=100, blank=True, null=True)
    profileImage = models.ImageField(default="profile_pics/!happy-face.png", upload_to="profile_pics")
    gender = models.BooleanField(default=1, verbose_name="gender")
    is_active = models.BooleanField(default=0, verbose_name="can login")
    is_delete = models.BooleanField(default=0, verbose_name="is delete")

    def __str__(self):
        return self.username

    # Run after model is saved
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profileImage.path)  # open the current instance
        if img.height > 300 or img.width > 300:
            new_size = (300, 300)
            img.thumbnail(new_size)
            img.save(self.profileImage.path)


# UserFollow
# class UserFollow(models.Model):
#     # In API
#     auth = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
#     follow_to = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
#     follow_time = models.DateTimeField(auto_now_add=True)
#     is_followed = models.BooleanField(default=0)
#
#
# class UserFriends(models.Model):
#     # In API
#     auth = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
#     friend_to = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
#     is_agreed = models.BooleanField(default=0)
#     friend_time = models.DateTimeField(auto_now_add=True)
#     modify_time = models.DateTimeField(auto_now=True)
