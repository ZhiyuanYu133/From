#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import JsonResponse
from rest_framework import generics
from rest_framework.decorators import api_view

from . import models
from . import serializers


class PostsView(generics.RetrieveAPIView):
    """
    detail
    """
    queryset = models.Posts.objects.all()
    serializer_class = serializers.PostsSerializer
    lookup_field = 'pk'
    print(lookup_field)


@api_view(['GET', 'POST'])
# @permission_classes([AllowAny])
def create_post(request):
    return JsonResponse({"state": 1})
