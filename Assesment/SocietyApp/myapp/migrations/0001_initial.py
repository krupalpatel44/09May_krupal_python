# Generated by Django 5.1.1 on 2024-10-17 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="registerdata",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("firstname", models.CharField(max_length=30)),
                ("lastname", models.CharField(max_length=30)),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=50)),
                ("mobile", models.BigIntegerField()),
                ("dob", models.DateField()),
                ("city", models.CharField(max_length=20)),
                ("gender", models.CharField(max_length=20)),
                ("address", models.TextField()),
                ("aadhar", models.BigIntegerField()),
                ("familytype", models.CharField(max_length=20)),
                (
                    "image",
                    models.FileField(
                        default="/static/img/userprofile.png",
                        upload_to="Image/Members Photos/",
                    ),
                ),
            ],
        ),
    ]
