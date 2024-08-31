from django.urls import path

from . import views

app_name = "notes"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:note_id>/", views.NotesView.as_view(), name="notes"),
    path("update/<int:notes_id>/", views.UpdateView.as_view(), name="update"),
    path("create/", views.CreateView.as_view(), name="create"),
]
