from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PersonSerializer, ClubSerializer
from .models import Person, Club

# Create your views here.
class PersonView (viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class ClubView (viewsets.ModelViewSet):
    serializer_class = ClubSerializer
    queryset = Club.objects.all()