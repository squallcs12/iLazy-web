from rest_framework import routers, serializers
from api import viewsets, models


class AppSerializer(serializers.HyperlinkedModelSerializer):
    price = serializers.DecimalField(max_digits=5, decimal_places=2, coerce_to_string=False)

    class Meta:
        model = models.App
        fields = ('id', 'name', 'site', 'price')


class FilterContains(object):
    field = 'site'

    def filter_queryset(self, request, queryset, view):
        value = request.GET.get(self.field)
        if value:
            query_filter = {
                "%s__contains" % self.field: value
            }
            queryset = queryset.filter(**query_filter)
        return queryset


class AppViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.App.objects.all()
    serializer_class = AppSerializer
    filter_backends = (FilterContains, )


router = routers.DefaultRouter()
router.register(r'apps', AppViewSet)
