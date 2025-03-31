from django.contrib import admin
from django.contrib.auth import views
from django.urls import path,include

app_name = 'accounts'
urlpatterns = [
    path("register/",views.RegisterUserView.as_view(),name="register-user"),
]