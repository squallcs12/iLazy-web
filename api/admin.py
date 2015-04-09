from django.contrib import admin
from api import models


class AppAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')


admin.site.register(models.App, AppAdmin)
