from django.db import models
from rest_framework.response import Response as OriginResponse


class Response(OriginResponse):

    SERIALIZERS = {}

    @classmethod
    def register_serializers(cls, *serializers):
        for serializer in serializers:
            cls.SERIALIZERS[serializer.Meta.model] = serializer

    def serialize_object(self, obj, context):
        return self.SERIALIZERS[obj.__class__](obj, context=context).data

    def __init__(self, data=None, context=None, **kwargs):
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, models.Model):
                    data[key] = self.serialize_object(value, context)
            if 'errors' in data:
                data['success'] = False
            else:
                data['success'] = True
        super(Response, self).__init__(data=data, **kwargs)
