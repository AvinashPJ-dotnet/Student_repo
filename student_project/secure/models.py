from django.db import models

# Create your models here.

class Secure(models.Model):
    entity_id = models.CharField(max_length=30, blank=False)
    username = models.CharField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False)