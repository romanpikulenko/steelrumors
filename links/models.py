import imp
from tkinter import CASCADE

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count


# Create your models here.
class LinkVoteCountManager(models.Manager):
    def get_queryset(self):
        return super(LinkVoteCountManager, self).get_queryset().annotate(votes=Count("vote")).order_by("-votes")


class Link(models.Model):
    title = models.CharField("Headline", max_length=100)
    submitter = models.ForeignKey(User, on_delete=models.CASCADE)
    submitted_on = models.DateTimeField(auto_now_add=True)
    rank_score = models.FloatField(default=0.0)
    url = models.URLField("URL", max_length=250, blank=True)
    description = models.TextField(blank=True)

    with_votes = LinkVoteCountManager()
    objects = models.Manager()

    def __str__(self):
        return self.title


class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.ForeignKey(Link, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.voter.username} upvoted {self.link.title}"
