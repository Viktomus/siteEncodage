from django.db import models
from django.forms import ModelForm
from django.forms import FileInput
from django import forms

class Document(models.Model):
    doc = models.FileField(upload_to='files/',blank=False)

class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ('doc',)