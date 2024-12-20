# Generated by Django 4.0 on 2024-09-14 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_userregister_lastname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ourservices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('blood', models.CharField(max_length=100)),
                ('urine', models.CharField(max_length=100)),
                ('xray', models.CharField(max_length=100)),
                ('ultrasound', models.CharField(max_length=100)),
                ('ctscan', models.CharField(max_length=100)),
                ('thayroid', models.CharField(max_length=100)),
                ('calcium', models.CharField(max_length=100)),
                ('crp', models.CharField(max_length=100)),
            ],
        ),
    ]
