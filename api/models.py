from django.conf import settings
from django.db import models


class App(models.Model):
    name = models.CharField(max_length=255)
    site = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    price_life = models.DecimalField(max_digits=5, decimal_places=2, default=10.0)
    introduction = models.TextField(default='')
    request_sites = models.TextField(default='')
    require_params = models.TextField(default='')
    command = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name


class UserApp(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    app = models.ForeignKey(App)

    class Meta:
        unique_together = (('user', 'app'), )


class Result(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    app = models.ForeignKey(App)
    result = models.TextField(default='')
