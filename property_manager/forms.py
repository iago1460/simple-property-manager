from django import forms
from leaflet.forms.widgets import LeafletWidget
from property_manager.models import Property
from django.utils.translation import ugettext_lazy as _


class PropertyForm(forms.ModelForm):

    class Meta:
        model = Property
        fields = ('name', 'geom', 'description',)
        widgets = {'geom': LeafletWidget()}


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label=_('username'))
    password = forms.CharField(required=True, label=_('password'), widget=forms.PasswordInput)