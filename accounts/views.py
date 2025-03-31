from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .forms import UserRegisterForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class RegisterUserView(CreateView):
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:user-login')
    form_class = UserRegisterForm
    success_message = "User Create Successfully.Thank You"