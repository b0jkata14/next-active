from cloudinary.uploader import destroy
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.contrib.auth import get_user_model


from next_active.accounts.models import UserProfile

UserModel = get_user_model()


# @receiver(pre_save, sender=UserProfile)
# def delete_old_profile_picture(sender, instance, **kwargs):
#     if instance.pk:
#         old_profile_picture = UserProfile.objects.get(pk=instance.pk).profile_picture
#         if old_profile_picture != instance.profile_picture:
#             old_image_public_id = old_profile_picture.public_id if old_profile_picture else None
#             if old_image_public_id:
#                 destroy(old_image_public_id)


@receiver(post_save, sender=UserModel)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


#  Проблем при първа регистрация проверява дали има снимка, става въпрос сигнала за триене на стара снимка
