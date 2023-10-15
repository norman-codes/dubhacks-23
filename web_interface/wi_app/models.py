import uuid
from django.db import models
from django.urls.base import reverse

# Create your models here.

class Recording(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    voice_recording = models.FileField(upload_to="recordings")

    class Meta:
        verbose_name = "Recording"
        verbose_name_plural = "Recordings"

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("recording_detail", kwargs={"id": str(self.id)})