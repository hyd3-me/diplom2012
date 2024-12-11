from django import forms
from django.contrib.auth.models import User

from .models import FixGroup


class GroupCreationForm(forms.ModelForm):

    group_pwd = forms.CharField(label='Пароль', max_length=64,
            widget=forms.PasswordInput())

    class Meta:
        model = FixGroup
        fields = ('name',)
