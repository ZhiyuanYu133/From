#!/usr/bin/env python
# -*- coding: utf-8 -*-


from rest_framework import serializers

from home.models import UserInbux, User, UserFollow, UserFriends
from stream.models import Posts
from .models import Comment, LikeHistory


class PostsSerializer(serializers.ModelSerializer):
    type = serializers.CharField(max_length=10, default='posts')

    class Meta:
        model = Posts
        fields = ('uuid', 'title', 'source', 'id', 'origin', 'description', 'contentType', 'content',
                  'categories', 'author', 'view_count', 'like_count', 'comment_count', 'published', 'image',
                  "visibility", "is_public", "CommonMark", "is_friends_public", "type")


class UserInbuxSerializer(serializers.ModelSerializer):
    type = serializers.CharField(default='author', max_length=10)

    class Meta:
        model = UserInbux
        fields = ('type', 'uuid', 'id', 'url', 'host', 'github', 'profileImage', 'displayName')


class Usererializer(serializers.ModelSerializer):
    type = serializers.CharField(default='author', max_length=10)

    class Meta:
        model = User
        fields = ('type', 'uuid', 'id', 'url', 'host', 'github', 'profileImage', 'displayName')


class Commenterializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('uuid', 'type', 'author', 'post', 'comment', 'contentType', 'published', 'id')


class LikedSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeHistory
        fields = ('context', 'type', 'summary', 'author', 'object')


class FollowRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollow
        fields = ('belongTo', 'type', 'summary', 'actor', 'object')


class FriendsRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFriends
        fields = ('belongTo', 'type', 'summary', 'actor', 'object')
