# Generated by Django 4.1.5 on 2023-02-26 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TwitterAccountChecked",
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
                ("screen_name", models.CharField(max_length=100)),
            ],
        ),
    ]
