import datetime

from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic

from notes.forms import (
    CreateForm,
    NotesForm,
)
from notes.models import NotesModel


class IndexView(generic.View):

    def get(self, request):
        queryset = NotesModel.objects.order_by("last_modified").last()
        return redirect("notes:notes", note_id=queryset.id)


class NotesView(generic.View):
    template_name = "notes/notes.html"
    success_url = reverse_lazy("notes:notes")
    form_class = NotesForm

    def get(self, request, note_id):
        queryset = NotesModel.objects.get(id=note_id)
        form = NotesForm(instance=queryset)
        notes_names = NotesModel.objects.values("id", "name")
        return render(request, self.template_name, {"form": form, "notes_names": notes_names})


class UpdateView(generic.UpdateView):

    def post(self, request, notes_id):
        form_name = request.POST.get("name")
        form_text = request.POST.get("text")
        NotesModel.objects.filter(id=notes_id).update(name=form_name, text=form_text, last_modified=timezone.now())
        data = NotesModel.objects.filter(id=notes_id).values("name", "text")
        return JsonResponse({"name": data[0]["name"], "text": data[0]["text"]})


class CreateView(generic.CreateView):
    model = NotesModel
    form_class = CreateForm
    template_name = "notes/create.html"
    success_url = reverse_lazy("notes:notes")
