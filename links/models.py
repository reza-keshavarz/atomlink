from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Link(models.Model):
    title = models.CharField(max_length=40)
    destination = models.CharField(max_length=300)
    description = models.CharField(max_length=140, null=True, blank=True)
    author = models.ForeignKey(User, related_name = 'links_links')
    publish = models.DateTimeField(default = timezone.now())

    def __str__(self):
        return self.title

class AdLink(models.Model):
    title = models.CharField(max_length=40)
    destination = models.CharField(max_length=300)
    description = models.CharField(max_length=300, null=True, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User)
    list_title = models.CharField(max_length=40)
    bio = models.CharField(max_length=200)

    def __str__(self):
        return self.list_title
