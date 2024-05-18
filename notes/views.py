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
    queryset = NotesModel.objects.order_by("last_modified").last()

    def get(self, request):
        form = NotesForm(instance=self.queryset)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form_name = request.POST.get("name")
        form_text = request.POST.get("text")
        NotesModel.objects.update_or_create(
            name=form_name,
            defaults={"text": form_text},
        )
        return redirect("notes:index")
