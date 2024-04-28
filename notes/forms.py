from django import forms
from django.contrib.auth.forms import UserCreationForm

from notes.models import NotesModel


class NotesForm(forms.Form):
    name = forms.CharField(label="", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Name"}))
    notes_text = forms.CharField(
        label="", widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Text"})
    )

    class Meta:
        model = NotesModel
        fields = ("name", "text")
