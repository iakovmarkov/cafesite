from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewset, EventViewset

router = DefaultRouter()
router.register(r'menu', MenuItemViewset)
router.register(r'events', EventViewset)

urlpatterns = [
    path("", include(router.urls)),
]