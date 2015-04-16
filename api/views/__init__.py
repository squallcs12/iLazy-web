from rest_framework import routers, serializers
from api import viewsets, models


class AppSerializer(serializers.HyperlinkedModelSerializer):
    price = serializers.DecimalField(max_digits=5, decimal_places=2, coerce_to_string=False)

    class Meta:
        model = models.App
        fields = ('id', 'name', 'site', 'price')


class AppDetailSerializer(serializers.HyperlinkedModelSerializer):
    price = serializers.DecimalField(max_digits=5, decimal_places=2, coerce_to_string=False)
    price_life = serializers.DecimalField(max_digits=5, decimal_places=2, coerce_to_string=False)

    class Meta:
        model = models.App
        fields = ('id', 'name', 'site', 'price', 'price_life', 'introduction', 'request_sites', 'require_params')


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
    serializer_class = AppSerializer
    serializer_class_single = AppDetailSerializer
    filter_backends = (filter_contain('site'), )


class MyAppViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.App.objects.all()
    serializer_class = AppDetailSerializer

    def get_queryset(self):
        user_app_ids = self.request.user.userapp_set.all().values_list('app_id')
        return models.App.objects.all().filter(id__in=user_app_ids)


router = routers.DefaultRouter()
router.register(r'apps', AppViewSet)
router.register(r'my_apps', MyAppViewSet)
