from django.conf.urls import include, url
from api.views import router
from api.views.app_execute_view import AppExecuteView
from api.views.login_view import LoginView

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^execute/', AppExecuteView.as_view(), name='execute'),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^login/', LoginView.as_view(), name='login'),
]
