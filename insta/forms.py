from django import forms
from .models import Profile,Image


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['belongs_to']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes', 'profile']

