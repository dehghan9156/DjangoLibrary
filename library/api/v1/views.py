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
from .serialization import BookSerializer,AmanatSerializer
from library.models import Book,Amanat,Category
from accounts.models import Profile,User

class ListBookApiView(generics.ListAPIView):
    model = Book
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class DetailBookApiView(generics.RetrieveAPIView):
    model = Book
    serializer_class = BookSerializer
    queryset = Book.objects.all()

# class AmanatBookApiView(CreateAPIView):
#     serializer_class = AmanatSerializer
#     permission_classes = [IsAuthenticated]
#
#     def get_serializer_context(self):
#         context = super().get_serializer_context()
#         book = get_object_or_404(Book, pk=self.kwargs['pk'])
#         context.update({
#             'book': book,
#         })
#         return context

class ShowAmanatApiView(generics.ListAPIView):
    model = Amanat
    serializer_class = AmanatSerializer
    queryset = Amanat.objects.all()

    def get_queryset(self, *args, **kwargs):
        profile = get_object_or_404(Profile,user=self.request.user)
        amanat = Amanat.objects.filter(profile=profile)
        return amanat

