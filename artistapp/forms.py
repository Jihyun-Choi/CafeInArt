from django.forms import ModelForm
from django import forms

from artistapp.models import Artist


class ArtistCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-left',
                                                           'style': 'height: auto;'}))

    class Meta:
        model = Artist
        fields = ['name', 'category', 'phone_number',
                  'image1', 'image2', 'image3', 'image4', 'content']