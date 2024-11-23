# Generated by Django 5.1.1 on 2024-10-28 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="watchman",
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
                ("firstname", models.CharField(max_length=20)),
                ("lastname", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                ("dob", models.DateField()),
                ("mobile", models.BigIntegerField()),
                ("aadhar", models.BigIntegerField()),
                ("gender", models.CharField(max_length=20)),
                (
                    "image",
                    models.FileField(
                        default="/static/img/watchmanprofile.png",
                        upload_to="Image/watchman Photos/",
                    ),
                ),
            ],
        ),
    ]
