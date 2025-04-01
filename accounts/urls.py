from django.contrib import admin
from . import views
from django.urls import path,include

app_name = 'accounts'
urlpatterns = [
    path("register/",views.RegisterUserView.as_view(),name="register-user"),
    path("login/",views.LoginUserView.as_view(),name="login-user"),
    path("logout/",views.LogoutUserView.as_view(),name="logout-user"),
    path("profile/",views.ProfileUserView.as_view(),name="profile-user"),
]