# Generated by Django 4.2.2 on 2023-06-30 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Daily",
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
                ("numberofcups", models.IntegerField()),
                ("numberofsleeping", models.IntegerField()),
            ],
        ),
    ]