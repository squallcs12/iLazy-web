from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'ilazy_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('api.urls', namespace='apps')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
