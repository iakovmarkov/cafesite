from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateTimeField()
    
    def __str__(self):
        return f'{self.title} on {self.date}'

class MenuItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.title} for {self.price} CZK'