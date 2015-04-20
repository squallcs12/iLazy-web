from datetime import timedelta
from django.http.response import HttpResponseBadRequest
from django.utils import timezone
from rest_framework import status
from rest_framework.views import APIView
from api.forms import AppPurchaseForm
from api.models import Result, UserApp, UserCoinsHistory
from api.response import Response
from api.tasks import execute_app


class AppPurchaseView(APIView):
    def post(self, request):
        """
        Execute app from user
        ---
        response_serializer: api.serializers.ResultSerializer

        parameters:
            - name: app
              type: integer
            - name: params
              type: string
        """
        form = AppPurchaseForm(request.POST)
        if not form.is_valid():
            return HttpResponseBadRequest()

        data = form.cleaned_data
        app = data['app']
        is_life = data.get('kind') == 'life'

        if is_life:
            price = app.price_life
            extend = None
        else:
            price = app.price
            extend = timedelta(days=30)

        now = timezone.now().date()

        try:
            user_app = UserApp.objects.get(user=request.user, app=app)
            if extend is None:  # buy life
                if user_app.expires >= now:  # already buy month
                    histories = UserCoinsHistory.objects.filter(user=request.user, refer_id=app.id,
                                                                kind=UserCoinsHistory.KIND_BUY_APP)
                    history = histories.latest("id")
                    price -= history.cost  # reduce the price include refun
                user_app.expires = None
            else:
                if user_app.expires >= now:
                    user_app.expires = user_app.expires + extend
                else:
                    user_app.expires = now + extend
        except UserApp.DoesNotExist:
            if extend is None:
                expires = None
            else:
                expires = now + extend

            user_app = UserApp(user=request.user, app=app, expires=expires)

        if request.user.coins < price:
            return Response({
                'errors': [{
                    'code': 'NOT_ENOUGH_COINS',
                    'message': 'You need more %s coin(s) to buy this app.' % (price - request.user.coins),
                }]
            }, status=status.HTTP_402_PAYMENT_REQUIRED)

        request.user.coins -= price
        request.user.save()

        UserCoinsHistory.objects.create(user=request.user, cost=price, remain=request.user.coins, refer_id=app.id,
                                        kind=UserCoinsHistory.KIND_BUY_APP)

        user_app.save()

        return Response({
            'user_app': user_app
        }, context={'request': request})
