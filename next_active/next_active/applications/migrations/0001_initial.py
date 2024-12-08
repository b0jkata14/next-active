# Generated by Django 5.1.3 on 2024-11-27 20:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainerApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport', models.CharField(choices=[('Лека атлетика', 'Лека атлетика'), ('Бадминтон', 'Бадминтон'), ('Баскетбол', 'Баскетбол'), ('Бокс', 'Бокс'), ('Борба', 'Борба'), ('Гимнастика', 'Гимнастика'), ('Гребане', 'Гребане'), ('Джудо', 'Джудо'), ('Плуване', 'Плуване'), ('Парапланеризъм', 'Парапланеризъм'), ('Ръгби', 'Ръгби'), ('Стрелба', 'Стрелба'), ('Сноуборд', 'Сноуборд'), ('Ски', 'Ски'), ('Тенис на маса', 'Тенис на маса'), ('Тенис', 'Тенис'), ('Таекуондо', 'Таекуондо'), ('Волейбол', 'Волейбол'), ('Вдигане на тежести', 'Вдигане на тежести'), ('Хандбал', 'Хандбал'), ('Езда', 'Езда'), ('Хокей на лед', 'Хокей на лед'), ('Шахмат', 'Шахмат'), ('Колоездене', 'Колоездене'), ('Фитнес', 'Фитнес'), ('Футбол', 'Футбол'), ('Фехтовка', 'Фехтовка'), ('Йога', 'Йога'), ('Карате', 'Карате'), ('Друго', 'Друго')], max_length=100)),
                ('certifications', models.TextField()),
                ('application_date', models.DateTimeField(auto_now_add=True)),
                ('is_pending', models.BooleanField(default=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
                ('decision_date', models.DateTimeField(blank=True, null=True)),
                ('message', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
