from django.conf.urls import url 
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewset, EventViewset, contact

router = DefaultRouter()
router.register(r'menu', MenuItemViewset)
router.register(r'events', EventViewset)

urlpatterns = [
    url("contact", contact),
    path("", include(router.urls)),
]