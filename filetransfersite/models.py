from django.db import models

# Create your models here.
class files(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/')