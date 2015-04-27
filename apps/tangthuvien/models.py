from django.conf import settings
from django.db import models


class Topic(models.Model):
    topic_id = models.PositiveIntegerField()
    last_post_id = models.PositiveIntegerField(default=0)
    last_page_number = models.PositiveIntegerField(default=0)


class TopicUser(models.Model):
    topic = models.ForeignKey(Topic)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
