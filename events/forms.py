from django import forms
from cloudinary.forms import CloudinaryFileField

from .models import Event


class EventForm(forms.ModelForm):
    description = forms.CharField(strip=False, widget=forms.Textarea)
    photo = CloudinaryFileField()


    class Meta:
        model = Event
        exclude = ['host']
