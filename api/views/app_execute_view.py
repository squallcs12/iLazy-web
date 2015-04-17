from django.http.response import HttpResponseBadRequest
from rest_framework import status
from rest_framework.views import APIView
from api.forms import AppExecuteForm
from api.models import Result
from api.response import Response
from api.tasks import execute_app


class AppExecuteView(APIView):
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
        form = AppExecuteForm(request.POST)
        if not form.is_valid():
            return HttpResponseBadRequest()

        data = form.cleaned_data
        app = data['app']
        if not request.user.userapp_set.filter(app=app).count():
            return Response({
                'errors': [{
                    'code': 'NOT_OWN_APP_EXECUTION',
                    'message': 'You need to own this application before using it.',
                }],
            }, status=status.HTTP_401_UNAUTHORIZED)

        result = Result.objects.create(app=app, user=request.user)
        execute_app.delay(result.id, json_params=data['json_params'])

        return Response({
            'result': result
        })
