from django.conf.urls import url 
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewset, EventViewset, CommentViewset, contact

router = DefaultRouter()
router.register(r'menu', MenuItemViewset)
router.register(r'events', EventViewset)

urlpatterns = [
    url("contact", contact),
    path("", include(router.urls)),
    re_path('^comments/(?P<event>.+)/$', CommentViewset.as_view()),
]