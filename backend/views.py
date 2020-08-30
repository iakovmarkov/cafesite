from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import MenuItemSerializer, EventSerializer
from .models import MenuItem, Event

def health(request):
    return HttpResponse("ok")

class MenuItemViewset(viewsets.ModelViewSet):
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()

class EventViewset(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()