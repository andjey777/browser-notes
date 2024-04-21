from django.shortcuts import (
    redirect,
    render,
)
from django.urls import reverse_lazy
from django.views import generic

from notes.forms import NotesForm
from notes.models import NotesModel


class IndexView(generic.CreateView):
    template_name = "notes/index.html"
    model = NotesModel
    success_url = reverse_lazy("notes:index")

    def get(self, request):
        form = NotesForm
        return render(request, self.template_name, {'form': form})

    def post(self, request):

        return redirect("notes:index")
