from django.shortcuts import render, get_object_or_404
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
import json

# Create your views here.


class CreateView(APIView):
    def post(self, request, format=None):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ListView(ListAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    pagination_class = TodoPagination


class SingleDataView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            todo_data = get_object_or_404(TodoModel, pk=kwargs['pk'])
            data = TodoSerializer(todo_data).data
            return Response(data, status=status.HTTP_200_OK)
        except:
            return Response('Nothing to show', status=status.HTTP_400_BAD_REQUEST)

