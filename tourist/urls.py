from django.urls import path
from .views import tourist_home


urlpatterns = [
    path('', tourist_home, name='tourist_home'),
]