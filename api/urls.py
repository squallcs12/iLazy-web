from django.conf.urls import include, url
from api.views import router

urlpatterns = [
    url(r'^', include(router.urls)),
]
