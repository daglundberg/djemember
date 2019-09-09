from django.utils.encoding import force_text
from django.db import models
from core.models import User


class TimelineItem(models.Model):
    date = models.DateTimeField('timeline date', blank=True, null=True)


class Memory(TimelineItem):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,)
    is_comment_on = models.ForeignKey("TimelineItem", on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    text = models.TextField()


class Picture(models.Model):
    timeline_item = models.OneToOneField(TimelineItem, on_delete=models.SET_NULL, primary_key=False, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,)
    memory = models.ForeignKey("Memory", on_delete=models.CASCADE, related_name='pictures', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', null=True)
    date = models.DateTimeField('creation date', blank=True, null=True)
    location = models.CharField(max_length=80, null=True, blank=True)
    gps_data = models.CharField(max_length=500, null=True, blank=True)
    caption = models.CharField(max_length=230, null=True, blank=True)


class Milestone(TimelineItem):
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    caption = models.CharField(max_length=230, null=True, blank=True)


class Chapter(Milestone):
    background_image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    background_class = models.CharField(max_length=12, null=True, blank=True)
