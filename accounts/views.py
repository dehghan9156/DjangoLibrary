from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages

from .forms import UserRegisterForm,LoginUserForm,ProfileUserForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import Profile
from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterUserView(View):
    form_class = UserRegisterForm
    template_name = "accounts/register.html"

    def get(self, request):
        form = self.form_class()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['email'], cd['password'])
            messages.success(request, 'User Register Successfully', 'success')
            return redirect('accounts:login-user')
        else:
            messages.error(request, 'User not found', 'error')
            return render(request, 'accounts/register.html', {'form': form})


class LoginUserView(View):
    def get(self,request):
        form = LoginUserForm()
        return render(request,'accounts/login.html',{'form':form})

    def post(self,request):
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['email'],password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'User Login Successfully', 'success')
                return redirect('library:list-books')
            else:
                messages.error(request, 'User not found', 'error')
        else:
            messages.error(request, 'Invalid form submission', 'error')

        return render(request, 'accounts/login.html', {'form': form})

class LogoutUserView(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        messages.success(request,"User Logout Successfully.",'success')
        return redirect('accounts:login-user')

class ProfileUserView(LoginRequiredMixin,View):
    def get(self,request):
        user = get_object_or_404(User,pk=self.request.user.pk)
        profile = Profile.objects.get(user=user)
        form = ProfileUserForm(instance=profile)
        return render(request,'accounts/profile.html',{'form':form,'profile':profile})

    def post(self,request):
        user = get_object_or_404(User,pk=self.request.user.pk)
        profile = Profile.objects.get(user=user)
        form = ProfileUserForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile Edith Successfully.",'success')
        else:
            messages.error(request,"Information Not Valid.",'error')
        return render(request,'accounts/profile.html',{'form':form,'profile':profile})

