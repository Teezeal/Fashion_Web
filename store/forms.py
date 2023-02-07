from django import forms
from .models import Clothes

class ClothesForms(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = "__all__"