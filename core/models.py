from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    connection_to_deceased = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    is_activated = models.BooleanField(default=False)
    avatar_url = models.CharField(max_length=256, blank=True, null=True)
