
from django.urls import path
from .views import parks

urlpatterns = [
    path("", parks),
]
