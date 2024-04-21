from django import forms
from django.contrib.auth.forms import UserCreationForm

from notes.models import NotesModel


class NotesForm(forms.Form):
    notes_text = forms.CharField(label="Input note:", widget=forms.TextInput(attrs={"class": "form-control"}))
