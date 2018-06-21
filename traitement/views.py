from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, Http404

from .models import Document,DocumentForm
from .appLib import *

maxSize = 50
maxSizeUnit = 2 #Mo

def index(request):#toujours mettre problem=True, sauf quand le traitement est terminé
    if request.method == 'POST':
        form = DocumentForm(request.POST or None, request.FILES)

        if form.is_valid():
            file = form.cleaned_data['doc']
            newEncoding = form.cleaned_data['newEncodingField']
            size,unit = getFileSizeUnit(file.size)
            form.save()

            if size > maxSize and (unit >= maxSizeUnit):
                return render(request, 'index.html', {'form': form, 'erreur': True, 'problem': True, 
                    'erreurMsg': "Fichier trop volumineux ! ({0}".format(size) + getUnitFromInt(unit) + ")"})

            downloadUrl = ''
            canDownload = None
            name = file.name
            size = file.size
            encoding,errorMsg = getFileEncoding(file)
            size,unit = getFileSizeUnit(size)

            if encoding == None:
                encoding = 'utf8'

            #Erreurs d'encodage
            if errorMsg != "":
                    return render(request, 'index.html', {'form': form, 'problem': True, 'erreur': True,
                        'erreurMsg': errorMsg, 'url': "http://" + request.get_host() + "/index"})

            if newEncoding != '':
                errorMsg = changeFileEncoding(file,encoding,newEncoding)

                if errorMsg != '':
                    return render(request, 'index.html', {'form': form, 'erreur': True, 'problem': True, 
                    'erreurMsg': errorMsg})
                else:
                    canDownload = True
                    downloadUrl = getFilePath(file)
    
            return render(request, 'index.html', {'form': form, 'problem': None,
                'nom': name, 'taille': size, 'encodage': encoding, 'unite': getUnitFromInt(unit), 
                'candownload': canDownload , 'downloadurl': downloadUrl
                })

    else:
        form = DocumentForm()
    return render(request, 'index.html', {'form': form, 'problem': True})