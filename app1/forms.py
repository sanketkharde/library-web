from django import forms
from .models import Books


class Bookform(forms.ModelForm):
    class Meta:
        model = Books
        fields ="__all__"