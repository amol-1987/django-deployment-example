from django.db import models

# Create your models here.
class User(models.Model):
    first = models.CharField(max_length=120)
    last = models.CharField(max_length=120)
    emailid = models.EmailField(max_length=260)
