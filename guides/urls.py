from django.urls import path
from .views import guides_list, guide_detail


urlpatterns = [
    path('', guides_list, name='guides_list'),
    path('<int:guide_id>/', guide_detail, name='guide_detail'),
]
