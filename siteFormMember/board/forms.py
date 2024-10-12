from django import forms
from .models import Board

class SaveForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ["title", "content"]