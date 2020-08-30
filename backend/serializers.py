from rest_framework import serializers
from .models import MenuItem, Event


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ("id", "title", "description", "price")


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("id", "title", "description", "date")