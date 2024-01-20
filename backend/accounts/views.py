from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserInfoSerializer


# Create your views here.
class UserInfoView(APIView):
    def get(self, request, username):
        user = User.objects.get(username=username)
        serializer = UserInfoSerializer(user)
        return Response(serializer.data)

