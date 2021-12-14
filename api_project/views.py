from django.shortcuts import render
from rest_framework import viewsets
import django_filters
import generics

from api_project.serializers import UserSerializer
from api_project.models import User

# class UserViewSet(viewsets.ModelViewSet):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer
#    # sort = query_params.get('sort','')
#    # queryset = queryset.order_by(sort)
#    # print(queryset)

#    def get_queryset(self):
#       # pass
#       queryset = self.get_queryset()
#       print(queryset)
#       sort = self.request.query_params.get('sort','')
#       print(sort)
#       if sort:
#          queryset = queryset.order_by(sort)
#       print(queryset)
#       return queryset

class UserViewSet(generics.ListCreateAPIView):
   model = User
   serializer_class = UserSerializer

