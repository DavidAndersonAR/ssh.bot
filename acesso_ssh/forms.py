from django import forms
from . models import AtivoEnel

class AtivoEnelModelForm(forms.ModelForm):

    class Meta:
        model = AtivoEnel
        fields = '__all__'





