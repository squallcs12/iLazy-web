from django.contrib import admin
from api import models


class AppAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'site', 'price')
    search_fields = ('id', 'name', 'site')


class UserAppAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'app')
    search_fields = ('id', 'app__name', 'user__username')


class UserCoinsHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'app', 'cost', 'remain', 'kind', 'refer_id')


admin.site.register(models.App, AppAdmin)
admin.site.register(models.UserApp, UserAppAdmin)
admin.site.register(models.UserCoinsHistory, UserCoinsHistoryAdmin)
