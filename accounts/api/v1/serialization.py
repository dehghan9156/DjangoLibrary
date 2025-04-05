from rest_framework import serializers
from accounts.models import User,Profile


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=250, write_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "confirm_password"]

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError("Those passwords don't match.")
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password', None)
        return User.objects.create_user(**validated_data)

class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["email","password"]

class ProfileUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["first_name","last_name","description","image","created_date"]
        read_only_fields = ["created_date"]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['full_name'] = instance.first_name+" "+instance.last_name
        return rep