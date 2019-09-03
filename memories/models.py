from django.utils.encoding import force_text
from django.db import models
from core.models import User


class Memory(models.Model):
    date = models.DateTimeField('timeline date')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,)
    pub_date = models.DateTimeField('date published')
    caption = models.CharField(max_length=230, null=True, blank=True)


class Text(Memory):
    long_text = models.TextField()


class Picture(Memory):
    url = models.CharField(max_length=200)
    location = models.CharField(max_length=80, null=True, blank=True)


class Milestone(Memory):
    image_url = models.CharField(max_length=200, null=True, blank=True)


class Chapter(Milestone):
    background_image_url = models.CharField(max_length=200)
