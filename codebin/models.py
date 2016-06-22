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
    last_edited_date = models.DateTimeField(null=True)
    base58 = models.CharField(default=make_base58, max_length=64, editable=False, primary_key=True)
    content = models.TextField()

    author = models.ForeignKey('auth.User', null=True)

    PRIVATE = 'PR'
    WITH_LINK = 'URL'
    PUBLIC = 'PUB'
    PRIVATE_CHOICE = [(PRIVATE, 'Private'), (WITH_LINK, 'Available by link'), (PUBLIC, 'Public')]
    private = models.CharField(max_length=3, choices=PRIVATE_CHOICE, default=PUBLIC)

    def __str__(self):
        return "Snippet {base}".format(base=self.base58)
