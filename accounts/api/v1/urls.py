from django.contrib import admin
from . import views
from django.urls import path,include

app_name = 'api-v1'
urlpatterns = [
    path("register/",views.RegisterUserApiView.as_view(),name="register-user-api"),
    path("login/",views.LoginUserApiView.as_view(),name="login-user-view"),
    path("logout/",views.LogoutUserApiView.as_view(),name="logout-user-view"),
    path("profile/",views.ProfileUserApiView.as_view(),name="profile-user-view"),

]