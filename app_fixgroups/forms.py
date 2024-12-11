from django import forms
from django.contrib.auth.models import User

from .models import FixGroup


class GroupCreationForm(forms.ModelForm):

    group_pwd   = forms.CharField(label='password', max_length=64,
            widget=forms.PasswordInput())

    class Meta:
        model   = FixGroup
        fields  = ('name',)

class GroupForm(forms.Form):

    name        = forms.CharField(label='name', max_length=32)
    group_pwd   = forms.CharField(label='password', max_length=64,
            widget=forms.PasswordInput())