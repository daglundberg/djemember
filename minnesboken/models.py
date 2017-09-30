from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import cloudinary
import cloudinary.uploader
import cloudinary.api

try:
    from django.utils.encoding import force_text
except ImportError:
    from django.utils.encoding import force_unicode as force_text


@python_2_unicode_compatible
class CloudinaryPhoto(models.Model):
    image = CloudinaryField('image')

    def __str__(self):
        return "Cloudinary photo"


@python_2_unicode_compatible
class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile')
    avatar_url = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return force_text(self.user.username)

    class Meta():
        db_table = 'user_profile'


@python_2_unicode_compatible
class Memory(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, blank=True, null=True,)
    pub_date = models.DateTimeField('date published')
    text = models.TextField()
    is_on_timeline = models.BooleanField(default=False)
    timeline_date = models.DateTimeField('date taken', null=True)

    def __str__(self):
        return force_text(self.pub_date)


@python_2_unicode_compatible
class Picture(models.Model):
    memory = models.ForeignKey(Memory, on_delete=models.SET_NULL, blank=True, null=True,)
    url = models.CharField(max_length=200)
    picture_text = models.CharField(max_length=230)
    picture_location = models.CharField(max_length=80)
    date_taken = models.DateTimeField('date taken')

    def __str__(self):
        return self.url


@python_2_unicode_compatible
class Writing(models.Model):
    memory = models.ForeignKey(Memory, on_delete=models.SET_NULL, blank=True, null=True,)
    title = models.CharField(max_length=62)
    text = models.TextField()

    def __str__(self):
        return self.title
