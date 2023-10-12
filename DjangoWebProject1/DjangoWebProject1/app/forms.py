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

class ListSearch(forms.Form):
    CHOICES=((0,'Любой'),(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),(8,'8'),(9,'9'),(10,'10'),(11,'11'))
    school=forms.CharField(max_length=10,min_length=None,label="Школа", required=False,
                           widget=forms.TextInput({
                               'class':'form-control',
                               'placeholder': 'Номер школы'}))
    fio=forms.CharField(max_length=100,min_length=None,label="ФИО", required=False,
                           widget=forms.TextInput({
                               'class':'form-control',
                               'placeholder': 'ФИО'}))
    cls=forms.ChoiceField(choices=CHOICES, label='Класс',
                           widget=forms.Select({
                               'class':'form-control'}))