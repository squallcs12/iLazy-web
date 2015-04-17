from django.contrib.auth import get_user_model, login
from django.contrib.auth.forms import AuthenticationForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers, status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from api.response import Response


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')


class LoginView(APIView):

    permission_classes = (AllowAny, )

    @method_decorator(csrf_exempt)
    def post(self, request):
        """
        Login into system
        ---
        parameters:
            - name: username
              type: string
            - name: password
              type: string
        """
        form = AuthenticationForm(request, request.POST)
        if not form.is_valid():
            return Response({
                'errors': [{
                    'code': 'WRONG_USERNAME_OR_PASSWORD',
                    'message': 'Username or password is not correct.'
                }]
            }, status=status.HTTP_401_UNAUTHORIZED)
        user = form.get_user()
        login(request, user)

        return Response({
            'user': UserSerializer(user).data
        })
