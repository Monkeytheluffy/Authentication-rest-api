from django.shortcuts import render
from rest_framework.response import Response
from .models import*
from .serializers import*
from rest_framework import status
from rest_framework import viewsets
# from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication


class Studentviewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    # authentication_classes=[BasicAuthentication]
    # premission_classes=[IsAuthenticated]

    authentication_classes=[SessionAuthentication]
    premission_classes=[IsAuthenticated]