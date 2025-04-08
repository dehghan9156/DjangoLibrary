from rest_framework import serializers
from library.models import Amanat,Book,Category


class BookSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(),slug_field="name")
    class Meta:
        model = Book
        fields = ["category","name","image","description","year","pages","created_date"]

class AmanatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amanat
        fields = ["profile","book","startdate","returndate","status"]