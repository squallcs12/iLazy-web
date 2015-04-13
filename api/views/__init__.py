from rest_framework import routers, serializers
from api import viewsets, models


class AppSerializer(serializers.HyperlinkedModelSerializer):
    price = serializers.DecimalField(max_digits=5, decimal_places=2, coerce_to_string=False)

    class Meta:
        model = models.App
        fields = ('id', 'name', 'site', 'price')


class AppViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.App.objects.all()
    serializer_class = AppSerializer

router = routers.DefaultRouter()
router.register(r'apps', AppViewSet)
