from django.db import models
from accounts.models import Profile,User

test_choice = (
    (1,("borrowed")),
    (2,("returned"))
)
class Amanat(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    book = models.ForeignKey('Book',on_delete=models.CASCADE)
    startdate = models.DateTimeField()
    returndate = models.DateTimeField()
    status = models.IntegerField(choices=test_choice)

    def __str__(self):
        return f"{self.book}-{self.status}"

class Book(models.Model):
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    image = models.URLField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    year = models.DateTimeField(blank=True,null=True)
    pages = models.IntegerField(blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pk}-{self.name}"

class Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return f"{self.name}"


