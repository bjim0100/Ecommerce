from tokenize import Token

from knox.auth import TokenAuthentication
from knox.views import LoginView as KnoxLoginView
from django.contrib import messages, auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins, status, permissions, viewsets, filters
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.conf import settings

from authentication.models import ProfileModel
from authentication.serializers import UserSerializer, LoginSerializer, ProfileSerializer, UserlistSerializer


class RegisterView(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request):
        return self.create(request)


class ProfileView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    serializer_class = ProfileSerializer
    queryset = ProfileModel
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [BasicAuthentication, SessionAuthentication]

    def post(self, request):
        return self.create(request)

    def update(self, request):
        return self.update(request)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)

# class UserList(generics.GenericAPIView,mixins.ListModelMixin):
#     serializer_class = UserlistSerializer
#     queryset = User.objects.all()
#
#     def list(self, request):
#         return self.list(request)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter]
    search_fields =  ['username', 'email']

    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_superuser:
    #         return User.objects.all()
    #     return User.objects.filter(username=user.username)
    #
    # def get_object(self):
    #     obj = get_object_or_404(User.objects.filter(id=self.kwargs["pk"]))
    #     self.check_object_permissions(self.request, obj)
    #     return obj

