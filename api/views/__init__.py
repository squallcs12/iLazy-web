from rest_framework import routers

from api import viewsets, models, serializers


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

router = routers.DefaultRouter()
router.register(r'apps', AppViewSet)
router.register(r'my_apps', MyAppViewSet, base_name='my_app')
