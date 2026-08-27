from django.db import models
from django.contrib.auth.models import User
from tourism.models import TourismPlace


class Itinerary(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='itineraries'
    )

    name = models.CharField(
        max_length=150,
        default='My Kimberley Trip'
    )

    start_date = models.DateField(
        blank=True,
        null=True
    )

    end_date = models.DateField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.name}"


class ItineraryItem(models.Model):

    itinerary = models.ForeignKey(
        Itinerary,
        on_delete=models.CASCADE,
        related_name='items'
    )

    place = models.ForeignKey(
        TourismPlace,
        on_delete=models.CASCADE,
        related_name='itinerary_items'
    )

    visit_date = models.DateField(
        blank=True,
        null=True
    )

    notes = models.TextField(
        blank=True
    )

    order = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['order', 'visit_date']

    def __str__(self):
        return f"{self.itinerary.name} - {self.place.name}"