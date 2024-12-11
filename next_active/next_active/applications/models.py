from django.contrib.auth import get_user_model
from django.db import models

from next_active.applications.choices import SportChoices

UserModel = get_user_model()


class TrainerApplication(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name="applications",
    )

    sport = models.CharField(
        max_length=100,
        choices=SportChoices.choices,
    )

    certifications = models.TextField()

    application_date = models.DateTimeField(
        auto_now_add=True,
    )

    is_pending = models.BooleanField(default=True)
    is_approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)

    decision_date = models.DateTimeField(
        blank=True,
        null=True
    )

    message = models.TextField(
        default='Your coaching request is being processed.',
    )

    def __str__(self):
        return (
            f"Application by {self.user.full_name}, "
            f"sport: {self.sport}, "
            f"created on {self.application_date}"
        )
