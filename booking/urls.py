from django.urls import path
from .views import book_guide, my_bookings, cancel_booking


urlpatterns = [
    path('book/<int:guide_id>/', book_guide, name='book_guide'),
    path('my-bookings/', my_bookings, name='my_bookings'),
    path('cancel/<int:booking_id>/', cancel_booking, name='cancel_booking'),
]
