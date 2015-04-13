from django.contrib import admin
from api import models


class AppAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'site', 'price')
    search_fields = ('id', 'name', 'site')


admin.site.register(models.App, AppAdmin)
