from http.client import responses
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404
from django.template.context_processors import request
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.generics import CreateAPIView,ListAPIView
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .serialization import BookSerializer
from library.models import Book,Amanat,Category


class ListBookApiView(generics.ListAPIView):
    model = Book
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class DetailBookApiView(generics.RetrieveAPIView):
    model = Book
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class AmanatBookApiView(APIView):
    def get(self,pk):
        pass
    def post(self,pk):
        pass