from django.contrib import admin
from api import models


class AppAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'site', 'price')
    search_fields = ('id', 'name', 'site')


class UserAppAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'app')
    search_fields = ('id', 'app__name', 'user__username')


class UserCoinsHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'cost', 'remain', 'kind', 'refer_id')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'website', 'price', 'email', )
    search_fields = ('user__username', 'website', 'email')


admin.site.register(models.App, AppAdmin)
admin.site.register(models.UserApp, UserAppAdmin)
admin.site.register(models.UserCoinsHistory, UserCoinsHistoryAdmin)
admin.site.register(models.Order, OrderAdmin)
