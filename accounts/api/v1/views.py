from http.client import responses
from django.conf import settings
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404
from django.template.context_processors import request
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.mail import send_mail
from rest_framework.generics import CreateAPIView
from .serialization import UserSerializer,LoginUserSerializer,ProfileUserSerializer
from django.contrib.auth import authenticate, login,logout
from accounts.models import User,Profile
class RegisterUserApiView(generics.GenericAPIView):
    serializer_class = UserSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data['email']
            data = {"email": email}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginUserApiView(generics.GenericAPIView):
    serializer_class = LoginUserSerializer
    permission_classes = [AllowAny]
    def post(self,request):
        serializer= self.serializer_class(data=request.data)
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request,username=email,password=password)
        if user is not None:
            login(request, user)
            return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)

        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

class LogoutUserApiView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        logout(request)
        return Response({"message":"Logout successfully"},status=status.HTTP_200_OK)

class ProfileUserApiView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileUserSerializer
    def get_object(self):
        profile = get_object_or_404(Profile,user=self.request.user)
        return profile