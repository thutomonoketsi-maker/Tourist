from django.contrib import admin
from .models import TourismPlace, SavedPlace


@admin.register(TourismPlace)
class TourismPlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'location', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'location')


@admin.register(SavedPlace)
class SavedPlaceAdmin(admin.ModelAdmin):
    list_display = ('user', 'place', 'saved_at')
