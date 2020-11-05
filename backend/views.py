from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from .serializers import MenuItemSerializer, EventSerializer, CommentSerializer
from .models import MenuItem, Event, Comment

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

class CommentViewset(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    def get_queryset(self):
        event = self.kwargs['event']
        return Comment.objects.filter(event=event)
    
    def perform_create(self, serializer):
        event = Event.objects.get(pk=self.kwargs['event'])
        date = datetime.now()
        print(date, event)
        serializer.save(event=event, date=date)