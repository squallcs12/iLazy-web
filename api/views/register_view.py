from django.contrib.auth import get_user_model, login
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from api.forms import RegistrationForm
from api.response import Response


class RegisterView(APIView):

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
        form = RegistrationForm(request.data)
        if not form.is_valid():
            return Response({
                'errors': form
            }, status=status.HTTP_400_BAD_REQUEST)
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        form.save_m2m()

        return Response({
            'user': user
        })
