from django import forms
from .models import Profile,Image


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['belongs_to']