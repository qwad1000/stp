from django.db import models

# Create your models here.
from django.utils import timezone


class Snippet(models.Model):
    title = models.CharField(max_length=128)
    save_name = models.CharField(max_length=128)
    created_date = models.DateTimeField(default=timezone.now)

