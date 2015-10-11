from django.db import models

from django.utils.encoding import smart_text

# Create your models here.


class Page(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True, unique=True)
    header_image = models.CharField(max_length=255, blank=False, null=False, default='&black')
    title = models.CharField(max_length=255, blank=False, null=False)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    edited = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return smart_text('%s' % (self.name,))


class SocialMediaButton(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    type = models.CharField(max_length=150, blank=False, null=False)
    account = models.CharField(max_length=150, blank=False, null=False)
    url = models.URLField(max_length=255, blank=False, null=False)

    def __str__(self):
        return smart_text('%s - %s' % (self.type, self.account,))
