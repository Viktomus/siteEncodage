from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, Http404

from .models import Document,DocumentForm
from .encodingLib import *

def confirm(request,name,size,encoding):
    unit = 'o'
    koSize = 1000
    moSize = 1000000
    goSize = 1000000000

    if size >= koSize and size < moSize:
        unit = 'Ko'
        size /= koSize
    elif size >= moSize and size < goSize:
        unit = 'Mo'
        size /= moSize
    elif size >= goSize:
        unit = 'Go'
        size /= goSize
    size = int(size)
    indexPage = 'http://' + request.get_host() + '/index'

    if encoding == 'None':
        encoding = 'UTF-8'
    else:
        encoding = encoding.upper()

    return render(request, 'confirm.html', {'nom': name, 'taille': size, 'encodage': encoding, 'unite': unit, 'accueil': indexPage})

def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            file = form.cleaned_data['doc']
            nom = file.name
            taille = file.size
            encodage = getFileEncoding(file)
            return redirect(confirm,name=nom,size=taille,encoding=encodage)
    else:
        form = DocumentForm()
    return render(request, 'index.html', {'form': form})