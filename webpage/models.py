from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=240)
    email = models.EmailField()