from django.db import models
from django.utils.encoding import smart_text
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    # model for your simple blog post
    title = models.CharField(max_length=255, blank=False, null=False)
    body = models.TextField(blank=False, null=False)
    header_image = models.CharField(max_length=255, blank=False, null=False, default='&black')
    user = models.ForeignKey(User, blank=False, null=False)
    created = models.DateTimeField(blank=False, null=False)
    edited = models.DateTimeField(blank=True, null=True)
    comments_enabled = models.BooleanField(blank=False, null=False, default=False)

    def __str__(self):
        return smart_text("%s" % (self.title,))


class Comment(models.Model):
    # model for comments on a post
    # will not be shown if Post.comments_enabled is False
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(null=False, blank=False)
    timestamp = models.DateTimeField(blank=False, null=False)
    post = models.ForeignKey(Post, blank=False, null=False)
    comment = models.TextField(blank=False, null=False)

    def __str__(self):
        return smart_text("%s - %s" % (self.post.id, self.comment[:50],))
