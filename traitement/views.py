from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, Http404

from .forms import SiteForm
from .appLib import *

import json
import urllib

maxSize = 50
maxSizeUnit = 2 #Mo
googleKey = '6LdvG2AUAAAAAFqh6C28wj78SivoGmA2xX6xC3Oz'#clé google captcha

def index(request):#toujours mettre problem=True, sauf quand le traitement est terminé
    webaddress = getWebAddress(request)

    if request.method == 'POST':
        form = SiteForm(request.POST, request.FILES)

        if form.is_valid():
            file = form.cleaned_data['document']
            size,unit = getFileSizeUnit(file.size)

            if size > maxSize and (unit >= maxSizeUnit):#si le fichier est trop volumineux
                return render(request, 'index.html', {'form': form, 'erreur': True, 'problem': True, 
                    'erreurMsg': "Fichier trop volumineux ! (Max:{0}".format(maxSize) + getUnitFromInt(maxSi) + ")",
                    'googlekey': googleKey, 'webaddress': webaddress
                    })

            name = file.name
            size = file.size
            encoding,errorMsg = getFileEncoding(file)
            size,unit = getFileSizeUnit(size)

            if encoding == None:
                encoding = 'utf8'
            else:
                try:
                    encoding = encoding.upper()
                except:
                    pass

            #Erreurs d'encodage
            if errorMsg != "":
                return render(request, 'index.html', {'form': form, 'problem': True, 'erreur': True,
                    'erreurMsg': errorMsg, 'url': "http://" + request.get_host() + "/index", 
                    'googlekey': googleKey, 'webaddress': webaddress})
    
            return render(request, 'index.html', {'form': form, 'problem': None,
                'nom': name, 'taille': size, 'encodage': encoding, 'unite': getUnitFromInt(unit) 
                ,'googlekey': googleKey, 'webaddress': webaddress
                })

    else:# methode n'est pas en POST
        form = SiteForm()
    return render(request, 'index.html', {'form': form, 'problem': True, 'googlekey': googleKey
        , 'webaddress': webaddress
        })