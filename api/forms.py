from django import forms

from api.models import App


class AppExecuteForm(forms.Form):
    app = forms.ModelChoiceField(queryset=App.objects.all())
    json_params = forms.CharField(required=False)


class AppPurchaseForm(forms.Form):
    app = forms.ModelChoiceField(queryset=App.objects.all())
    kind = forms.CharField(required=False)
