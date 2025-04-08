from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.template.context_processors import request
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from library.models import Amanat, Book, Category
from .forms import AmanatForm
from accounts.models import Profile,User
from datetime import timedelta


class ListBooksView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, "library/books.html", {'books': books})


class DetailBooksView(View):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        return render(request, "library/detail.html", {'book': book})

class AmanatBooksView(View,LoginRequiredMixin):
    def get(self,request,pk):
        form = AmanatForm()
        return render(request, "library/amanat-form.html", {'form':form})

    def post(self,request,pk):
        book = get_object_or_404(Book,pk=pk)
        form = AmanatForm(request.POST)
        profile = get_object_or_404(Profile,user=self.request.user)
        if form.is_valid():
            amanat = form.save(commit=False)
            amanat.profile = profile
            amanat.book = book
            amanat.status = "borrowed"
            amanat.save()
            # print("وضعیت امانت:", amanat.status)
            messages.success(request,"You borrowed this book.Thank you")
            return redirect("library:detail-books",book.pk)
        return render(request, "library/amanat-form.html", {'form':form})

class ShowAmanatView(View,LoginRequiredMixin):
    def get(self,request):
        profile = get_object_or_404(Profile,user=self.request.user)
        amanat = Amanat.objects.filter(profile=profile)
        return render(request,"library/amanat-show.html",{'amanat':amanat})

class ReturnBookView(View):
    def post(self,request,pk_amanat):
        profile = get_object_or_404(Profile,user=self.request.user)
        amanat = get_object_or_404(Amanat,profile=profile,pk=pk_amanat)
        if amanat.status=="borrowed":
            amanat.status = "returned"
        amanat.save()
        messages.success(request,"successfully book returned.",'success')
        return redirect("library:show-amanat")

class ExtendBookView(View):
    def post(self,request,pk):
        profile = get_object_or_404(Profile,user=self.request.user)
        amanat = get_object_or_404(Amanat,profile=profile,status="borrowed")
        amanat.returndate += timedelta(days=7)  # ۷ روز به تاریخ بازگشت اضافه می‌کنیم
        amanat.save()
        messages.success(request, "Your loan has been extended by 7 days.")
        return redirect("library:show-amanat")
