from django.shortcuts import (
    redirect,
    render,
)
from django.views import generic


class IndexView(generic.View):
    template_name = "notes/index.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return redirect("notes:index")
