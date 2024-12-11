from django.contrib.auth import get_user_model
from django.db import models

from next_active.accounts.models import TrainerProfile


UserModel = get_user_model()


class Review(models.Model):
    to_trainer = models.ForeignKey(
        TrainerProfile,
        related_name='reviews',
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        related_name='reviews',
        on_delete=models.CASCADE,
    )

    rating = models.PositiveIntegerField(
        choices=[(i, str(i)) for i in range(1, 6)],
    )

    comment = models.TextField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"Review for {self.trainer.user.first_name} by {self.user.first_name}"

    class Meta:
        ordering = ['-created_at']


class Like(models.Model):
    to_trainer = models.ForeignKey(
        TrainerProfile,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
