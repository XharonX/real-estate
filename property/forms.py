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
    BedroomSelection = ((i, f'{i} Bedroom') for i in range(1, 10))
    BathroomSelection = ((i, f"{i} Bathroom") for i in range(1, 10))

    bedroom = forms.ChoiceField(choices=BedroomSelection, required=False, widget=forms.Select(attrs={
        'class': 'input'
    }))
    bathroom = forms.ChoiceField(choices=BathroomSelection, required=False, widget=forms.Select(attrs={
        'class': 'input'
    }))
    class Meta:
        model = Property
        fields = '__all__'
        exclude = ['created_at', 'user', ]
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
            }),
            'square_feet': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'eg. 60 x 40'
            }),
            'city': forms.Select( attrs={
                'class': 'input'
            }),
            'type': forms.Select(attrs={
                'class': 'input',

            }),
            'status': forms.Select(attrs={
                'class': 'input',
            }),
            'owner': forms.TextInput(attrs={
                'class': 'input',
            }),
            'purpose': forms.Select(attrs={
                'class': 'input',
            })
        }
        print(fields)


ImageInlineFormset = inlineformset_factory(Property, Image, form=ImageForm, extra=3, max_num=7, min_num=1, can_delete=False, can_delete_extra=True)
ServiceInlineFormset = inlineformset_factory(Property, Service, fields='__all__', extra=1, can_delete=False, can_delete_extra=True)
NearbyInlineFormset = inlineformset_factory(Property, Nearby, fields='__all__', extra=1, can_delete=False, can_delete_extra=True)

