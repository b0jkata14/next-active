from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model


from next_active.accounts.models import UserProfile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, full_name=instance.first_name + ' ' + instance.last_name)
