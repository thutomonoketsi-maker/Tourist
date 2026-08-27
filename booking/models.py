from django.db import models
from django.contrib.auth.models import User
from guides.models import GuideProfile


class Booking(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    tourist = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tourist_bookings'
    )

    guide = models.ForeignKey(
        GuideProfile,
        on_delete=models.CASCADE,
        related_name='bookings'
    )

    date = models.DateField()

    time = models.TimeField()

    number_of_people = models.PositiveIntegerField(
        default=1
    )

    message = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.tourist.get_full_name()} - {self.guide}"