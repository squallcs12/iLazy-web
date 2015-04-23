from django import forms
from django.contrib.auth import get_user_model

from api.models import App


class AppExecuteForm(forms.Form):
    app = forms.ModelChoiceField(queryset=App.objects.all())
    json_params = forms.CharField(required=False)


class AppPurchaseForm(forms.Form):
    app = forms.ModelChoiceField(queryset=App.objects.all())
    kind = forms.CharField(required=False)


class RegistrationForm(forms.ModelForm):
    """
    Base class for registering users.
    """
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')
