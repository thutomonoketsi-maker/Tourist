from django.db import models
from django.contrib.auth.models import User


class GuideProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='guide_profile'
    )

    bio = models.TextField(
        blank=True
    )

    phone_number = models.CharField(
        max_length=30,
        blank=True
    )

    location = models.CharField(
        max_length=150,
        default='Kimberley'
    )

    profile_image = models.ImageField(
        upload_to='guides/',
        blank=True,
        null=True
    )

    experience = models.PositiveIntegerField(
        default=0,
        help_text='Number of years of guiding experience'
    )

    is_available = models.BooleanField(
        default=True
    )

    is_approved = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.user.get_full_name() or self.user.username