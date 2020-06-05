from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import generics
from .serializers import userSerializer, activitySerializer
from .models import user, activity

class userViewSet(generics.ListAPIView):
    queryset = user.objects.all()
    serializer_class = userSerializer

'''
Django’s generic views... were developed as a shortcut for common usage patterns... They take certain common idioms and patterns
found in view development and abstract them so that you can quickly write common views of data without having to repeat yourself.

The generic views provided by REST framework allow you to quickly build API views that map closely to your database models.

ListAPIView
Used for read-only endpoints to represent a collection of model instances.

Provides a get method handler.

Extends: GenericAPIView
'''
