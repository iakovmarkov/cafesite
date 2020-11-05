from django.contrib import admin
from .models import MenuItem, MenuCategory, Event, Comment

# Register your models here.

admin.site.register(MenuItem)
admin.site.register(MenuCategory)
admin.site.register(Event)
admin.site.register(Comment)