from django.db import models
from django import forms
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
                if isinstance(data['errors'], (forms.Form, forms.ModelForm)):
                    errors = []
                    form = data['errors']
                    for error in form.non_field_errors():
                        pass
                    for field in form:
                        error = {
                            field.name: field.errors
                        }
                        errors.append(error)
                    data['errors'] = errors
            else:
                data['success'] = True
        super(Response, self).__init__(data=data, **kwargs)
