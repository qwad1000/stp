from django.db import models
import uuid
import base58
# Create your models here.
from django.utils import timezone
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


class Snippet(models.Model):
    title = models.CharField(max_length=128)
    save_name = models.CharField(max_length=128)
    created_date = models.DateTimeField(default=timezone.now)
    base58 = models.CharField(blank=True, max_length=64, editable=False)

    def save_file(self, content):
        content_file = ContentFile(content)
        if not self.base58:
            self.base58 = base58.b58encode(uuid.uuid4().bytes)
            self.save()

        default_storage.save(self.base58, content_file)

    def get_content(self):
        content = ""
        if self.base58:
            try:
                file = default_storage.open(self.base58)
                content = file.read()
            except IOError:
                pass

        return content

    def __str__(self):
        return self.title + " " + self.base58
