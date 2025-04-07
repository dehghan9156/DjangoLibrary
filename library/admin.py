from django.contrib import admin
from .models import Amanat,Book,Category
from django.contrib.admin import ModelAdmin


class CustomAmanat(ModelAdmin):
    search_fields = ("pk","profile","book","status")
    list_display = ('book', 'profile', 'startdate', 'returndate', 'status')  # اضافه کردن status
class CustomBook(ModelAdmin):
    search_fields = ("pk","category","name")

class CustomCategory(ModelAdmin):
    search_fields = ("pk","name")

admin.site.register(Amanat,CustomAmanat)
admin.site.register(Book,CustomBook)
admin.site.register(Category,CustomCategory)
