# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from appt.serializers import UserSerializer, GroupSerializer
from django.views import View
from rest_framework.request import Request

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class Login(View):
    def get(self,request):
        pass
