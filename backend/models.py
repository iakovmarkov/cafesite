from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=2000)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='images', null=True)
    
    def __str__(self):
        return f'{self.title} on {self.date}'

class MenuItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images', null=True)
    
    def __str__(self):
        return f'{self.title} - {self.price} CZK'