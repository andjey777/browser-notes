from django import forms
from django.contrib.auth.forms import UserCreationForm

from notes.models import NotesModel


class NotesForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Name"}))
    notes_text = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Text"}))

    class Meta:
        model = NotesModel
        fields = ("name", "text")
