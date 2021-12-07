from rest_framework import serializers
from .models import *
from rest_framework.pagination import PageNumberPagination


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = '__all__'


class TodoPagination(PageNumberPagination):
    page_size = 2
