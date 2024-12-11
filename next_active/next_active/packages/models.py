from django.contrib.auth import get_user_model
from django.db import models

from next_active.accounts.models import TrainerProfile

#
# PACKAGE_TYPE_CHOICES = [
#     ('individual', 'Individual Package'),       # Индивидуален пакет
#     ('group', 'Group Package'),                 # Групов пакет
#     ('online', 'Online Package'),               # Онлайн пакет
#     ('hybrid', 'Hybrid Package'),               # Комбиниран пакет
#     ('trial', 'Trial Package'),                 # Тестов пакет
#     ('monthly', 'Monthly Package'),             # Месечен пакет
#     ('beginner', 'Beginner Package'),           # Пакет за начинаещи
#     ('family', 'Family or Dual Package'),       # Семейни или двойни пакети
# ]

PACKAGE_TYPE_CHOICES = [
    ('light', 'Light Package'),         # Лек, базов пакет
    ('standard', 'Standard Package'),   # Стандартен пакет
    ('premium', 'Premium Package'),     # Премиум пакет
    ('pro', 'Pro Package'),             # Професионален пакет
    ('ultimate', 'Ultimate Package'),   # Ултимативен, всичко включено
    ('basic', 'Basic Package'),         # Основен, минимален пакет
    ('flex', 'Flex Package'),           # Гъвкав пакет
    ('unlimited', 'Unlimited Package'),  # Неограничен пакет
]


class Package(models.Model):
    user = models.ForeignKey(
        to=TrainerProfile,
        on_delete=models.CASCADE,
        related_name='packages',
    )

    package_type = models.CharField(
        max_length=100,
        choices=PACKAGE_TYPE_CHOICES,
    )

    description = models.TextField()

    training_type = models.CharField(max_length=50,)
    session_count = models.IntegerField()
    session_duration = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    @property
    def price_per_session(self):
        if self.session_count > 0:
            return self.price / self.session_count
        return 0

    def __str__(self):
        return f"{self.package_type} - {self.training_type}"
