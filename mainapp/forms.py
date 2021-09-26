from django.forms import ModelForm
from django import forms

from mainapp.models import GalleryCafe


class GalleryCafeCreationForm(ModelForm):
    image1 = forms.ImageField(label='', required=True)
    name = forms.CharField(label='카페 이름', max_length=15)
    location = forms.CharField(label='카페 위치', max_length=15)
    phone_number = forms.CharField(label='카페 번호', max_length=15)

    content = forms.CharField(label='카페 정보', max_length=100, widget=forms.Textarea(attrs={
        'class': 'editable text-left',
        'rows':5,
        'cols': 50,
        'placeholder': '100자 까지 등록 가능합니다'
    }))


    class Meta:
        model = GalleryCafe
        fields = ['image1', 'name', 'location', 'phone_number', 'start_date', 'end_date',
                  'content']
