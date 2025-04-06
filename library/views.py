from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from library.models import Amanat, Book, Category


class ListBooksView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, "library/books.html", {'books': books})


class DetailBooksView(View):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        return render(request, "library/detail.html", {'book': book})
