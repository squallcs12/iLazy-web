from django import forms

from api.models import App


class AppExecuteForm(forms.Form):
    app = forms.ModelChoiceField(queryset=App.objects.all())
    json_params = forms.CharField(required=False)
