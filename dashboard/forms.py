from django import forms
from .models import newPollsUnit

class PollForm(forms.ModelForm):
    class Meta:
        model = newPollsUnit
        fields = '__all__'