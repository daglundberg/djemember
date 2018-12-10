from django.utils.encoding import force_text
from django.db import models
from core.models import User


class Memory(models.Model):
    userprofile = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,)
    pub_date = models.DateTimeField('date published')
    text = models.TextField()
    timeline_date = models.DateTimeField('date taken', null=True, blank=True)
    is_featured_publicly = models.BooleanField(default=False)

    def __str__(self):
        return force_text(self.pub_date)


class Picture(models.Model):
    memory = models.ForeignKey(Memory, on_delete=models.SET_NULL, blank=True, null=True,)
    url = models.CharField(max_length=200)
    picture_text = models.CharField(max_length=230)
    picture_location = models.CharField(max_length=80)
    date_taken = models.DateTimeField('date taken')
    is_featured_publicly = models.BooleanField(default=False)

    def __str__(self):
        return self.url
