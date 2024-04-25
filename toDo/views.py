from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
from .serializers import ToDoSerializer
from .models import ToDo
from django.shortcuts import get_object_or_404
from users.models import User


class ToDoView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = ToDoSerializer

    # def get_queryset(self):
    #     # return ToDo.objects.filter(album_id=self.kwargs['pk'])

    def perform_create(self, serializer):
      serializer.save(user=self.request.user)

