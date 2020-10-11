from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializers import MenuItemSerializer, EventSerializer
from .models import MenuItem, Event

@api_view(['POST'])
def contact(request):
    print("Not Yet Implemented")
    return HttpResponse()

class MenuItemViewset(viewsets.ModelViewSet):
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()

class EventViewset(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()