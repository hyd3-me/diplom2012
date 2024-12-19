from django import forms

from .models import Revision, List, Record


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

class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ('name', 'barcode', 'count', 'note')
        widgets = {
                'note': forms.Textarea(attrs={'rows':3}),
                'name': forms.TextInput(attrs={'autofocus': ''})
                }
