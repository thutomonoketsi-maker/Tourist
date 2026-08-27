from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('tourist', 'guide', 'date', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('tourist__first_name', 'tourist__last_name')
