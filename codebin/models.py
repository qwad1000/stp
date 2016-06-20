from django.db import models
import uuid
import base58
# Create your models here.
from django.utils import timezone


def make_base58():
    return base58.b58encode(uuid.uuid4().bytes)


class Snippet(models.Model):
    title = models.CharField(max_length=128)
    file_name = models.CharField(max_length=128)
    created_date = models.DateTimeField(default=timezone.now)
    base58 = models.CharField(default=make_base58, max_length=64, editable=False)
    content = models.TextField()

    def __str__(self):
        return "Snippet {base}".format(base=self.base58)
