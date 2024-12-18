from django import forms

from .models import Revision


class CreateRevisionForm(forms.ModelForm):
    class Meta:
        model = Revision
        fields = ('name',)
        widgets = {
                'name': forms.DateInput(attrs=dict(type='date'))
                }