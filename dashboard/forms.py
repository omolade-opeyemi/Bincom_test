from django import forms
from .models import newPollingUnit

class PollForm(forms.ModelForm):
    class Meta:
        model = newPollingUnit
        fields = '__all__'