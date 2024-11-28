from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from next_active.accounts.models import TrainerProfile
from next_active.applications.models import TrainerApplication

UserModel = get_user_model()


@receiver(post_save, sender=TrainerApplication)
def create_trainer_profile(sender, instance, **kwargs):
    if instance.is_approved and not instance.user.is_trainer:
        TrainerProfile.objects.create(
            user=instance.user,
            sport=instance.sport,
            certifications=instance.certifications,
        )

        instance.user.is_trainer = True
        instance.user.save()
