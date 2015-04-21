from django.core.exceptions import PermissionDenied
from django.http.response import Http404
from django.utils.translation import ugettext_lazy as _
from rest_framework import routers, exceptions, status
import six

from api import viewsets, models, serializers
from api.response import Response


def filter_contain(field):
    class FilterContains(object):
        def filter_queryset(self, request, queryset, view):
            value = request.GET.get(field)
            if value:
                query_filter = {
                    "%s__contains" % field: value.lower()
                }
                queryset = queryset.filter(**query_filter)
            return queryset
    return FilterContains


class AppViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.App.objects.all()
    serializer_class = serializers.AppSerializer
    serializer_class_single = serializers.AppDetailSerializer
    filter_backends = (filter_contain('site'), )


class MyAppViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.UserApp.objects.none()
    serializer_class = serializers.UserAppSerializer

    lookup_field = 'app'

    def __init__(self, **kwargs):
        super(MyAppViewSet, self).__init__(**kwargs)
        self.skip_fetch_apps = False

    def dispatch(self, request, *args, **kwargs):
        if kwargs.get("app"):
            self.skip_fetch_apps = True
        return super(MyAppViewSet, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        user_apps = self.request.user.userapp_set.all()
        if self.skip_fetch_apps:
            return user_apps

        app_ids = [u.app_id for u in user_apps]
        apps = models.App.objects.all().filter(id__in=app_ids)
        for user_app in user_apps:
            for app in apps:
                if user_app.app_id == app.id:
                    user_app.app = app
        return user_apps


def exception_handler(exc, context):
    """
    Returns the response that should be used for any given exception.

    By default we handle the REST framework `APIException`, and also
    Django's built-in `ValidationError`, `Http404` and `PermissionDenied`
    exceptions.

    Any unhandled exceptions may return `None`, which will cause a 500 error
    to be raised.
    """
    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        if isinstance(exc.detail, list):
            data = {'errors': exc.detail}
        elif isinstance(exc.detail, dict):
            data = {'errors': [exc.detail]}
        else:
            data = {'errors': [{'message': exc.detail}]}

        return Response(data, status=exc.status_code, headers=headers)

    elif isinstance(exc, Http404):
        msg = _('Not found.')
        data = {'errors': [{'message': six.text_type(msg)}]}
        return Response(data, status=status.HTTP_404_NOT_FOUND)

    elif isinstance(exc, PermissionDenied):
        msg = _('Permission denied.')
        data = {'errors': [{'message': six.text_type(msg)}]}
        return Response(data, status=status.HTTP_403_FORBIDDEN)

    # Note: Unhandled exceptions will raise a 500 error.
    return None



router = routers.DefaultRouter()
router.register(r'apps', AppViewSet)
router.register(r'my_apps', MyAppViewSet, base_name='my_app')
