from rest_framework import serializers
from .models import MenuItem, Event, Comment


class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=False)
    class Meta:
        model = MenuItem
        fields = ("id", "title", "description", "category", "image", "price")


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("id", "title", "description", "excerpt", "date", "image")

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "name", "email", "text", "date")