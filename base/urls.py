from django.urls import path, include
from .views import datashower

urlpatterns = [
    path("shower/", datashower),
]