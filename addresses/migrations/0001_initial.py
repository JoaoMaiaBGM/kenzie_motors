# Generated by Django 4.1.5 on 2023-01-10 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
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
                ("state", models.CharField(max_length=50)),
                ("city", models.CharField(max_length=50)),
                ("street", models.CharField(max_length=127)),
                ("zip_code", models.CharField(max_length=8)),
                ("number", models.IntegerField(null=True)),
                ("complement", models.CharField(max_length=127)),
            ],
        ),
    ]