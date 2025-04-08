from django.contrib import admin
from . import views
from django.urls import path,include

app_name = 'api-v1'
urlpatterns = [
    path("books/",views.ListBookApiView.as_view(),name="list-book-api"),
    path("book/<int:pk>/",views.DetailBookApiView.as_view(),name="detail-book-api"),
    # path("amanat/<int:pk>/",views.AmanatBookApiView.as_view(),name="amanat-book-api"),
    path("show/amanat/",views.ShowAmanatApiView.as_view(),name="show-amanat-api"),
]