from django.db.models.query import QuerySet
from django.shortcuts import (
    redirect,
    render,
)
from django.urls import reverse_lazy
from django.views import generic

from notes.forms import NotesForm
from notes.models import NotesModel


class IndexView(generic.UpdateView):
    template_name = "notes/index.html"
    success_url = reverse_lazy("notes:index")

    def get_queryset(self):
        self.queryset = NotesModel.objects.latest("last_modified")

    def get(self, request):
        form = NotesForm
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form_name = request.POST.get("name")
        form_text = request.POST.get("notes_text")
        NotesModel.objects.update_or_create(
            name=form_name,
            defaults={"text": form_text},
        )
        return redirect("notes:index")
