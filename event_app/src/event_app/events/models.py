from __future__ import unicode_literals
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=128)
    date = models.DateTimeField()
    place = models.CharField(max_length=128)
# Create your models here.
