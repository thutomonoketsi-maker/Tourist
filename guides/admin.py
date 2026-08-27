from django.contrib import admin
from .models import GuideProfile


@admin.register(GuideProfile)
class GuideProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'experience', 'is_available', 'is_approved')
    list_filter = ('is_available', 'is_approved')
    search_fields = ('user__first_name', 'user__last_name', 'location')
