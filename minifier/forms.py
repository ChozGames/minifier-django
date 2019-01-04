from django import forms
from .models import Url


class UrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ('url','pseudo')

class CodeForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ('code',)