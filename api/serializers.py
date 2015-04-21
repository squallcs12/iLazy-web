from rest_framework import serializers

from api import models
from api.response import Response


class AppSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.App
        fields = ('id', 'name', 'site', 'price')


class AppDetailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.App
        fields = ('id', 'name', 'site', 'price', 'price_life', 'introduction', 'request_sites', 'require_params',
                  'responses')


class ResultSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Result
        fields = ('id', )


class UserAppSerializer(serializers.ModelSerializer):
    app = AppDetailSerializer(read_only=True)

    class Meta:
        model = models.UserApp
        fields = ('id', 'user', 'app', 'expires', 'expires_str')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = ('id', 'user', 'website', 'steps', 'email', 'price')


Response.register_serializers(AppSerializer, AppDetailSerializer, ResultSerializer, UserAppSerializer)
