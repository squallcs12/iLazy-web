from django.conf import settings
from django.db import models


class App(models.Model):
    name = models.CharField(max_length=255)
    site = models.CharField(max_length=255)
    price = models.IntegerField()
    price_life = models.IntegerField()
    introduction = models.TextField(default='')
    request_sites = models.TextField(default='')
    require_params = models.TextField(default='')
    command = models.CharField(max_length=255, default='')
    responses = models.TextField(default='')

    def __str__(self):
        return self.name


class UserApp(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    app = models.ForeignKey(App)
    expires = models.DateField(null=True)

    @property
    def expires_str(self):
        return self.expires.strftime("%b %d")

    class Meta:
        unique_together = (('user', 'app'), )


class Result(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    app = models.ForeignKey(App)
    result = models.TextField(default='')


class UserCoinsHistory(models.Model):
    KIND_BUY_APP = 1
    kind_choices = [(KIND_BUY_APP, 'Buy App')]

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    refer_id = models.IntegerField()
    cost = models.IntegerField()
    remain = models.IntegerField()
    kind = models.IntegerField(choices=kind_choices)
    date = models.DateTimeField(auto_now_add=True)
