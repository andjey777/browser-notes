from django.db import models

# Create your models here.


class NotesModel(models.Model):
    name = models.TextField()
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
