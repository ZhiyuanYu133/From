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
    follow_to_username = models.CharField(max_length=256)
    follow_time = models.DateTimeField(auto_now_add=True)
    is_followed = models.BooleanField(default=0)
    hosts = models.TextField(default="")
    follow_to_hosts = models.TextField(default="")

    @staticmethod
    def is_follows(user_id, follow_to):
        users = UserFollow.objects.filter(create_user=user_id, follow_to=follow_to)
        if users.exists():
            return True
        return False


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

    @staticmethod
    def is_friends(user_id, friend_to):
        users = UserFriends.objects.filter(create_user=user_id, friend_to=friend_to)
        if users.exists():
            return True
        return False

    @staticmethod
    def agree(id):
        user_friends = UserFriends.objects.filter(id=id)
        if not user_friends.exists():
            return False

        user_friends.update(
            is_agreed=1
        )
        user_friend = user_friends[0]
        userfriend = UserFriends(
            create_user=user_friend.friend_to,
            create_user_name=user_friend.friend_to_username,
            friend_to=user_friend.create_user,
            friend_to_username=user_friend.create_user_name,
            is_agreed=1,
        )
        userfriend.save()
        print("userfriend:{}".format(userfriend))


class UserInbux(models.Model):
    class Meta:
        ordering = ["-add_time", "-is_read"]

    create_user = models.CharField(max_length=256)
    create_username = models.CharField(max_length=256)
    operator = models.CharField(max_length=256)
    operator_username = models.CharField(max_length=256)
    action = models.CharField(max_length=256)
    url = models.TextField()
    detail = models.TextField()
    add_time = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=0)
    action_model = models.CharField(default="UserFriends", max_length=100)
    source_id = models.CharField(default="", max_length=100)

    @staticmethod
    def add_inbux(
            create_user,
            create_username,
            operator,
            operator_username,
            action,
            url,
            detail,
            source_id,
            action_model="UserFriends",
    ):
        inbux = UserInbux(
            create_user=create_user,
            create_username=create_username,
            operator=operator,
            operator_username=operator_username,
            action=action,
            url=url,
            detail=detail,
            action_model=action_model,
            source_id=source_id,
        )
        inbux.save()

    @staticmethod
    def update_state(user_id, id):
        inbuxs = UserInbux.objects.filter(operator=user_id, id=id)
        print("inbuxs:{}".format(inbuxs))
        if not inbuxs.exists():
            return False
        inbuxs.update(is_read=1)
        inbux = inbuxs[0]
        if inbux.action_model == "UserFriends":
            UserFriends.agree(inbux.source_id)


class Node(models.Model):
    class Meta:
        verbose_name_plural = 'Node'

    type = models.CharField(max_length=255, default="node", editable=False)
    host = models.CharField(primary_key=True, max_length=255, null=False)
    username = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f"type:{self.type} host:{self.host} username:{self.username} password:{self.password}"
