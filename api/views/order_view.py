from api import serializers
from api.viewsets import CreateAPIView


class OrderView(CreateAPIView):
    serializer_class = serializers.OrderSerializer
