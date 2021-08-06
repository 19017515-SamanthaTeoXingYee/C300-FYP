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


class SLAManagementForm(forms.Form):
    """Authentication form which uses boostrap CSS."""
    min_temperature = forms.CharField(label='Minimum Temperature', max_length=2,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Minimum Temperature...'}))
    max_temperature = forms.CharField(label='Maximum Temperature', max_length=2,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder':'Maximum temperature...'}))
