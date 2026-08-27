from django.urls import path
from .views import guide_home


urlpatterns = [
    path('', guide_home, name='guide_home'),
]