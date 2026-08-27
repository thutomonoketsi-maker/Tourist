from django.urls import path
from .views import my_trips, create_trip


urlpatterns = [
    path('', my_trips, name='my_trips'),
    path('create/', create_trip, name='create_trip'),
]