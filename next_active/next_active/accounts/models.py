from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser
from django.db import models

from next_active.accounts.manager import AppUserManager
from next_active.accounts.utils import profile_picture_folder
from next_active.applications.choices import SportChoices


class AppUser(AbstractUser):
    username = None

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

    objects = AppUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class UserProfile(models.Model):
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        related_name='profile',
        primary_key=True,
    )

    profile_picture = CloudinaryField(
        'image',
        transformation={
            'width': 500,
            'height': 500,
            'crop': 'limit',
            'quality': 'auto:good',
            'fetch_format': 'webp',
        },
        folder=profile_picture_folder,
        blank=True,
        null=True,
        default='https://res.cloudinary.com/dsyzcsr5w/image/upload/v1733430959/users/0/aqkxfvktpokyyzu3dmmx.jpg',
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

    location = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    experience = models.PositiveIntegerField(
        blank=True,
        null=True,
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

    @property
    def profile(self):
        return self.user.profile