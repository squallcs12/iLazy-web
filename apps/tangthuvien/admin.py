from django.contrib import admin

from apps.tangthuvien import models


admin.site.register(models.Topic)
admin.site.register(models.TopicUser)
