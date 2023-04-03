#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import generics
from rest_framework import viewsets

from . import models
from . import serializers


class APIList(generics.ListAPIView):
    queryset = models.Posts.objects.all()
    serializer_class = serializers.APISerializer


class APIDetail(generics.RetrieveAPIView):
    queryset = models.Posts.objects.all()
    serializer_class = serializers.APISerializer


class APIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Posts.objects.all()
    serializer_class = serializers.APISerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = models.Posts.objects.all()
    serializer_class = serializers.APISerializer
