from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages

from .forms import UserRegisterForm,LoginUserForm,ProfileUserForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import User,Profile

class RegisterUserView(CreateView):
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:user-login')
    form_class = UserRegisterForm
    success_message = "User Create Successfully.Thank You"

class LoginUserView(View):
    def get(self,request):
        form = LoginUserForm()
        return render(request,"accounts/login.html",{'form':form})

    def post(self,request):
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['email'],password=cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request,"User Login Successfully.",'success')
                return redirect('accounts:login-user')
            else:
                messages.error(request,"User Does Not Exist.",'error')
        else:
            messages.error(request,"Invalid form submission",'error')

class LogoutUserView(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        messages.success(request,"User Logout Successfully.",'success')
        return redirect('accounts:login-user')

class ProfileUserView(LoginRequiredMixin,View):
    def get(self,request):
        user = get_object_or_404(Profile,user=self.request.user)
        form = ProfileUserForm(instance=user)
        return render(request,'accounts/profile.html',{'form':form})

    def post(self,request):
        user = get_object_or_404(Profile,user=self.request.user)
        form = ProfileUserForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile Edith Successfully.",'success')
        else:
            messages.error(request,"Information Not Valid.",'error')
        return render(request,'accounts/profile.html',{'form':form})

