# Generated by Django 4.2.2 on 2023-06-13 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_baseuser_is_staff"),
    ]

    operations = [
        migrations.CreateModel(
            name="Publisher",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "base_user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="publisher",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="base user",
                    ),
                ),
            ],
            options={
                "verbose_name": "Publisher",
                "verbose_name_plural": "Publishers",
            },
        ),
        migrations.CreateModel(
            name="ContentManager",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "base_user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="content_manager",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="base user",
                    ),
                ),
            ],
            options={
                "verbose_name": "Content Manager",
                "verbose_name_plural": "Content Managers",
            },
        ),
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "base_user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="client",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="base user",
                    ),
                ),
            ],
            options={
                "verbose_name": "Client",
                "verbose_name_plural": "Clients",
            },
        ),
    ]
