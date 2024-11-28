from django.contrib.auth.models import AbstractUser
from django.db import models

from next_active.applications.choices import SportChoices


class AppUser(AbstractUser):
    email = models.EmailField(
        unique=True,
    )

    first_name = models.CharField(
        max_length=50,
    )

    last_name = models.CharField(
        max_length=50,
    )

    is_trainer = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        related_name='profile',
        primary_key=True,
    )

    profile_picture = models.ImageField(
        upload_to='#',
        blank=True,
        null=True
    )

    full_name = models.CharField(
        max_length=100,
    )

    bio = models.TextField(
        blank=True,
        null=True,
    )

    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"Profile: {self.user.username}"


class TrainerProfile(models.Model):
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        related_name='trainer',
        primary_key=True,
    )

    sport = models.CharField(
        max_length=100,
        choices=SportChoices.choices,
    )

    certifications = models.TextField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"Trainer: {self.user.username} - Sport: {self.sport}"
