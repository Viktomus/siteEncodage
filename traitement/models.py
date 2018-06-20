from django.db import models
from django.forms import ModelForm

class Document(models.Model):
    doc = models.FileField(upload_to='files/')

class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ('doc',)