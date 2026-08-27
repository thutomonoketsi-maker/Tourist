from django.db import models
from django.contrib.auth.models import User


class TourismPlace(models.Model):

    CATEGORY_CHOICES = [
        ('attraction', 'Attraction'),
        ('activity', 'Activity'),
        ('accommodation', 'Accommodation'),
        ('restaurant', 'Food & Dining'),
    ]

    name = models.CharField(max_length=150)

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )

    description = models.TextField()

    location = models.CharField(max_length=200)

    image = models.ImageField(
        upload_to='tourism/',
        blank=True,
        null=True
    )

    image_url = models.URLField(
        blank=True,
        default=''
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    contact_number = models.CharField(
        max_length=30,
        blank=True
    )

    website = models.URLField(
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name


class SavedPlace(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='saved_places'
    )

    place = models.ForeignKey(
        TourismPlace,
        on_delete=models.CASCADE,
        related_name='saved_by_users'
    )

    saved_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'place'],
                name='unique_saved_place'
            )
        ]
        ordering = ['-saved_at']

    def __str__(self):
        return f"{self.user.username} - {self.place.name}"