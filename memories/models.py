from django.utils.encoding import force_text
from django.db import models
from core.models import User


class TimelineItem(models.Model):
    date = models.DateTimeField('timeline date', blank=True, null=True)


class Memory(TimelineItem):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,)
    is_comment_on = models.ForeignKey("TimelineItem", on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    pub_date = models.DateTimeField('date published')
    text = models.TextField()


class Picture(models.Model):
    memory = models.ForeignKey("Memory", on_delete=models.CASCADE, related_name='pictures', blank=False, null=False)
    image = models.ImageField(upload_to='uploads/', null=True)
    date = models.DateTimeField('timeline date', blank=True, null=True)
    location = models.CharField(max_length=80, null=True, blank=True)
    caption = models.CharField(max_length=230, null=True, blank=True)


class Milestone(TimelineItem):
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    caption = models.CharField(max_length=230, null=True, blank=True)


class Chapter(Milestone):
    background_image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    background_class = models.CharField(max_length=12, null=True, blank=True)
