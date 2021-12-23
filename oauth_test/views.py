from django.contrib.auth.models import User, Group
from django.shortcuts import render

# Create your views here.
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework import generics, permissions

from oauth_test.serializers import UserSerializer, GroupSerializer


class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer