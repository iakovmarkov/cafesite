from rest_framework import serializers
from .models import MenuItem, Event


class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=False)
    class Meta:
        model = MenuItem
        fields = ("id", "title", "description", "category", "image", "price")


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("id", "title", "description", "excerpt", "date", "image")