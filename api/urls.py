from django.conf.urls import include, url
from api.views import router
from api.views.login_view import LoginView

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^login/', LoginView.as_view(), name='login'),
]
