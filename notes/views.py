from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from notes.forms import NotesForm, CreateForm
from notes.models import NotesModel


class IndexView(generic.UpdateView):
    template_name = "notes/index.html"
    success_url = reverse_lazy("notes:index")
    form_class = NotesForm

    def get(self, request):
        queryset = NotesModel.objects.order_by("last_modified").last()
        form = NotesForm(instance=queryset)
        return render(request, self.template_name, {"form": form})


class UpdateView(generic.UpdateView):

    def post(self, request, notes_id):
        form_name = request.POST.get("name")
        form_text = request.POST.get("text")
        NotesModel.objects.filter(id=notes_id).update(name=form_name, text=form_text)
        data = NotesModel.objects.filter(id=notes_id).values("name", "text")
        return JsonResponse({"name": data[0]["name"], "text": data[0]["text"]})


class CreateView(generic.CreateView):
    model = NotesModel
    form_class = CreateForm
    template_name = "notes/create.html"
    success_url = reverse_lazy("notes:index")
