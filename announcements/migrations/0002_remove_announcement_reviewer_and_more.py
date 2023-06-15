# Generated by Django 4.2.2 on 2023-06-15 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_publisher_contentmanager_client"),
        ("announcements", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="announcement",
            name="reviewer",
        ),
        migrations.AddField(
            model_name="announcement",
            name="assigned_reviewer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="announcements",
                to="accounts.contentmanager",
                verbose_name="assigned_reviewer",
            ),
        ),
    ]