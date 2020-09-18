from django.urls import path, include
from .views import datashower, dataposter

urlpatterns = [
    path("shower/", datashower),
    path("poster/", dataposter),
]