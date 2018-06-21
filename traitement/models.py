from django.db import models
from django.forms import ModelForm
from django.forms import FileInput

class Document(models.Model):
    doc = models.FileField(upload_to='files/',blank=False)
    newEncodingField = models.CharField(max_length=20,blank=True)

class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ('doc','newEncodingField', )