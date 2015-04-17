from rest_framework import serializers

from api import models
from api.response import Response


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


class ResultSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Result
        fields = ('id', )


Response.register_serializers(AppSerializer, AppDetailSerializer, ResultSerializer)
