from django.db import models

# Create your models here.
class files(models.Model):
    title = models.CharField(max_length=100)
    fileName = models.CharField(max_length=100)