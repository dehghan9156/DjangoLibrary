from rest_framework import serializers
from library.models import Amanat,Book,Category
from django.shortcuts import get_object_or_404
from accounts.models import Profile,User

class BookSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(),slug_field="name")
    class Meta:
        model = Book
        fields = ["category","name","image","description","year","pages","created_date"]

class AmanatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amanat
        fields = ["profile","book","startdate","returndate","status"]
#
#     def create(self, validated_data):
#         request = self.context.get('request')
#         profile = get_object_or_404(Profile,user=request.user)
#         book = self.context.get('book')
#         return Amanat.objects.create(
#             **validated_data,
#             profile=profile,
#             book=book,
#             status='borrowed'
#         )
#
