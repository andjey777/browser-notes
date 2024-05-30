from django import forms
from django.contrib.auth.forms import UserCreationForm

from notes.models import NotesModel


class NotesForm(forms.ModelForm):
    name = forms.CharField(
        label="", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Name", "readonly": "readonly"})
    )
    text = forms.CharField(label="", widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Text"}))

    class Meta:
        model = NotesModel
        fields = ("name", "text")


class CreateForm(forms.ModelForm):
    name = forms.CharField(
        label="Name Of Your Note", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Name"})
    )

    class Meta:
        model = NotesModel
        fields = ("name",)
