from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

CHOICES = (
    ("father", _('father')),
    ("mother", _('mother')),
    ("sister", _('sister')),
    ("brother", _('brother')),
    ("cousin", _('cousin')),
    ("neighbour", _('neighbour')),
)


class User(AbstractUser):
    connection_verbose = models.TextField(max_length=500, blank=True)
    connection_short = models.CharField(choices=CHOICES, max_length=16, blank=True)
    year_of_meeting = models.SmallIntegerField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True)
    avatar_url = models.CharField(max_length=256, blank=True, null=True)
