from django.db import models

# Create your models here.
class user(models.Model):
    userid = models.CharField(max_length=50)
    passward = models.CharField(max_length=50)