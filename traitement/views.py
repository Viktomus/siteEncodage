from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, Http404

from .models import Document,DocumentForm
from .filesManager import *

maxSize = 50
maxSizeUnit = 2 #Mo

def index(request):#toujours mettre problem=True, sauf quand le traitement est terminé
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            file = form.cleaned_data['doc']
            size,unit = getFileSizeUnit(file.size)

            if size > maxSize and (unit >= maxSizeUnit):
                return render(request, 'index.html', {'form': form, 'erreur': True, 'problem': True, 
                    'erreurMsg': "Fichier trop volumineux ! ({0}".format(size) + getUnitFromInt(unit) + ")"})

            name = file.name
            size = file.size
            encoding,errorMsg = getFileEncoding(file)
            size,unit=getFileSizeUnit(size)

            if encoding == 'None':
                encoding = 'Inconnu'
            else:
                encoding = encoding.upper()

            #Erreurs d'encodage
            if errorMsg != "":
                    return render(request, 'index.html', {'form': form, 'problem': True, 'erreur': True,
                        'erreurMsg': errorMsg, 'url': "http://" + request.get_host() + "/index"})
            return render(request, 'index.html', {'form': form, 'problem': None,
                'nom': name, 'taille': size, 'encodage': encoding, 'unite': getUnitFromInt(unit) 
                })

    else:
        form = DocumentForm()
    return render(request, 'index.html', {'form': form, 'problem': True})