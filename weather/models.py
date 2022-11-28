from django.db import models

# Create your models here.
class weather(models.Model):
    city = models.CharField(max_length=50)
    curr_temp = models.CharField(max_length=50)
