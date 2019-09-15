from django.db import models
from core.models import User


class Post(models.Model):
    timeline_date = models.DateTimeField('timeline date', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    text = models.TextField(blank=True)


class Picture(Post):
    is_in_album = models.ForeignKey("Album", on_delete=models.CASCADE, related_name='pictures', blank=True, null=True)

    image = models.ImageField(upload_to='uploads/pictures/', null=True)
    date_taken = models.DateTimeField('creation date', blank=True, null=True)
    location = models.CharField(max_length=80, null=True, blank=True)
    gps_data = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return 'Picture: ' + self.image.name


class Album(Post):
    title = models.CharField(max_length=50, null=True, blank=True)


class Milestone(Post):
    image = models.ImageField(upload_to='uploads/milestones/', null=True, blank=True)
    caption = models.CharField(max_length=250, null=True, blank=False)

    def __str__(self):
        return 'Milestone: ' + self.caption


class Chapter(Post):
    image = models.ImageField(upload_to='uploads/chapters/', null=True, blank=True)
    caption = models.CharField(max_length=250, null=True, blank=False)

    background_image = models.ImageField(upload_to='uploads/chapters/', null=True, blank=True)
    background_class = models.CharField(max_length=12, null=True, blank=True)
    # The "background_class" field exists in case a Chapter could use custom CSS styling, idea is primarily to use Bulma tags like is-dark and is-light, the problem is that:
    # TODO: background_class is injected straight in to the html and is a huge security vulnerability!
    # Currently Chapter objects can only be created by administrators so this isn't the biggest deal at the moment but..
    # ..some kind of html filter should still be implemented, or a list of CSS classes to pick from (instead of a CharField allowing anything).

    def __str__(self):
        return 'Chapter: ' + self.caption


class Quote(Post):
    quotee_name = models.CharField(max_length=50, null=True, blank=True)
    quotee_description = models.CharField(max_length=100, null=True, blank=True)

    background_image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    background_class = models.CharField(max_length=12, null=True, blank=True)


class Comment(models.Model):
    is_comment_on = models.ForeignKey("Post", on_delete=models.CASCADE, related_name='comments', blank=False, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    text = models.TextField()
