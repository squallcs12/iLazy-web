from rest_framework import routers, serializers, viewsets
from api.models import App


class AppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = App
        fields = ('id', 'name', 'price')


class AppViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer

router = routers.DefaultRouter()
router.register(r'apps', AppViewSet)
