"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class BootstrapFipyAdditionForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    deviceid = forms.CharField(max_length=6,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Device ID...'}))
    devicename = forms.CharField(label=_("Device Name..."),
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder':'Name your device...'}))
