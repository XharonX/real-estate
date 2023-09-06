from django import forms
from .models import *
from django.forms import inlineformset_factory

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'caption']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'input'}),
            'caption': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Caption (eg. living room)',
            })
        }


class PropertyForm(forms.ModelForm):

    class Meta:
        model = Property
        fields = ['name', 'address', 'price', 'google_map']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input',
            }),
            'address': forms.TextInput(attrs={
                'class': 'input',
            }),
            'price': forms.TextInput(attrs={
                'class': 'input',
            }),
            'google_map': forms.TextInput(attrs={
                'class': 'input',
            })
        }


ImageInlineForm = inlineformset_factory(Property, Image, form=ImageForm, extra=3, max_num=7, min_num=1, can_delete=False, can_delete_extra=True)
ServiceInlineForm = inlineformset_factory(Property, Service, fields='__all__', extra=1, can_delete=False, can_delete_extra=True)
NearbyInlineForm = inlineformset_factory(Property, Nearby, fields='__all__', extra=1, can_delete=False, can_delete_extra=True)

