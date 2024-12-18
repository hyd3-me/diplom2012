from django import forms

from .models import Revision, List


class CreateRevisionForm(forms.ModelForm):
    class Meta:
        model = Revision
        fields = ('name',)
        widgets = {
                'name': forms.DateInput(attrs=dict(type='date'))
                }

class CreateListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ('name',)
        widgets = {
                'name': forms.TextInput(attrs={'autofocus': ''})
                }
