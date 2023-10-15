from django.db import models

# Create your models here.
class UserAudioInput(models.Model):
    timestamp = models.CharField(max_length=200)  # this will be a unique id based on timestamp of user submission

    def __str__(self):
        return self.id
