from django.urls import path, include
from .views import datashower, dataposter, datadeleter

urlpatterns = [
    path("shower/", datashower),
    path("poster/", dataposter),
    path("deleter/<int:id>/", datadeleter)
]