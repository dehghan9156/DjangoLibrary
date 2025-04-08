from django.contrib import admin
from . import views
from django.urls import path,include

app_name = 'library'
urlpatterns = [
    path("books/",views.ListBooksView.as_view(),name="list-books"),
    path("detail/<int:pk>/",views.DetailBooksView.as_view(),name="detail-books"),
    path("amanat/<int:pk>/",views.AmanatBooksView.as_view(),name="amanat-books"),
    path("show/amanat/",views.ShowAmanatView.as_view(),name="show-amanat"),
    path("return/book/<int:pk_amanat>/",views.ReturnBookView.as_view(),name="return-book"),
    path("extend/book/<int:pk>/",views.ExtendBookView.as_view(),name="extend-book"),
    path("api/v1/",include("library.api.v1.urls",namespace="api-v1")),
]