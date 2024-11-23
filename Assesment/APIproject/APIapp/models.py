from django.db import models

# Create your models here.

class Task(models.Model):
    title=models.CharField(max_length=100)
    code=models.CharField(max_length=200)
    linenos=models.BooleanField(default=False)
    language=models.CharField(max_length=100)
    style=models.CharField(max_length=100)