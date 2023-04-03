#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers

from stream.models import Posts


class APIInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = "__all__"


class APISerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = "__all__"
