from django.db import models
from django import forms

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=2000)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='images', blank=True)
    
    def __str__(self):
        return f'{self.title} on {self.date}'


class MenuCategory(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, blank=True)
    
    def __str__(self):
        return self.title

class MenuItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, blank=True)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images', blank=True)
    category = models.ForeignKey(MenuCategory, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f'{self.title} - {self.price} CZK'