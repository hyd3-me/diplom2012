from django import forms
from app_controldate.models import ControlDate

class ControlDateForm(forms.ModelForm):
    class Meta:
        model = ControlDate
        fields = ('name', 'e_date')
        widgets = {
                'e_date': forms.DateInput(attrs=dict(type='date')),
                'name': forms.TextInput(attrs={'autofocus': ''})
                }
