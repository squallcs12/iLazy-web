from rest_framework import viewsets, mixins, status
from rest_framework.generics import GenericAPIView
from api.response import Response


class ListModelMixin(object):
    """
    List a queryset.
    """
    name_many = None

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if self.name_many is None:
            self.name_many = "%ss" % queryset.model._meta.object_name.lower()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({
            self.name_many: serializer.data
        })


class RetrieveModelMixin(object):
    """
    Retrieve a model instance.
    """
    name_single = None
    serializer_class_single = None

    def get_serializer_single(self, *args, **kwargs):
        if self.serializer_class_single is None:
            return self.get_serializer(*args, **kwargs)
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class_single(*args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        if self.name_single is None:
            self.name_single = instance.__class__.__name__.lower()

        serializer = self.get_serializer_single(instance)
        return Response({
            self.name_single: serializer.data
        })


class ReadOnlyModelViewSet(RetrieveModelMixin,
                           ListModelMixin,
                           viewsets.GenericViewSet
                           ):
    pass


class ModelViewSet(mixins.CreateModelMixin,
                   RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   ListModelMixin,
                   viewsets.GenericViewSet):
    pass


class CreateModelMixin(mixins.CreateModelMixin):
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            serializer.Meta.model.__name__.lower(): serializer.data
        }, status=status.HTTP_201_CREATED, headers=headers)


class CreateAPIView(CreateModelMixin,
                    GenericAPIView):
    """
    Concrete view for creating a model instance.
    """

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
