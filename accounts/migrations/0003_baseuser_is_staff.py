# Generated by Django 4.2.2 on 2023-06-13 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_alter_baseuser_role"),
    ]

    operations = [
        migrations.AddField(
            model_name="baseuser",
            name="is_staff",
            field=models.BooleanField(default=False, verbose_name="is staff"),
        ),
    ]
