from django.db import models
from django.utils.text import slugify

class Event(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    date = models.CharField(max_length=15)
    location = models.CharField(max_length=50)

    class Meta:
        db_table = "EVENTS"