from django import forms

from .models import Event


class EventForm(forms.ModelForm):
    description = forms.CharField(strip=False, widget=forms.Textarea)

    class Meta:
        model = Event
        exclude = ['host']
