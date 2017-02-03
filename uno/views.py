from django.shortcuts import render
from uno.models import Room
from uno.serializer import RoomSerializer,UserSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from uno.permission import *


# Create your views here.

class RoomList(generics.ListCreateAPIView):
    """docstring for Roomlist"""
    queryset=Room.objects.all()
    serializer_class = RoomSerializer
    
		
class RoomDetail(APIView):
    def get(self, request, num, format=None):
        a = Room.objects.get(id=num)
        tran = RoomSerializer(a)
        return Response(tran.data)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer