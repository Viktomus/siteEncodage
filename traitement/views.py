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
    if request.method == 'POST':
        form = SiteForm(request.POST, request.FILES)

        if form.is_valid():
            #google captcha
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            #fin google captcha

            if result['success']:#si le captcha est bon
                file = form.cleaned_data['document']
                size,unit = getFileSizeUnit(file.size)

                if size > maxSize and (unit >= maxSizeUnit):#si le fichier est trop volumineux
                    return render(request, 'index.html', {'form': form, 'erreur': True, 'problem': True, 
                        'erreurMsg': "Fichier trop volumineux ! (Max:{0}".format(maxSize) + getUnitFromInt(maxSi) + ")",
                        'googlekey': googleKey
                        })

                name = file.name
                size = file.size
                encoding,errorMsg = getFileEncoding(file)
                size,unit = getFileSizeUnit(size)

                if encoding == None:
                    encoding = 'utf8'

                #Erreurs d'encodage
                if errorMsg != "":
                    return render(request, 'index.html', {'form': form, 'problem': True, 'erreur': True,
                        'erreurMsg': errorMsg, 'url': "http://" + request.get_host() + "/index", 
                        'googlekey': googleKey})
    
                return render(request, 'index.html', {'form': form, 'problem': None,
                    'nom': name, 'taille': size, 'encodage': encoding, 'unite': getUnitFromInt(unit) 
                     ,'googlekey': googleKey
                    })
            else:#captcha pas bon
                return render(request, 'index.html', {'form': form, 'problem': True, 'googlekey': googleKey,
                    'captcha':False
                    })

    else:# methode n'est pas en POST
        form = SiteForm()
    return render(request, 'index.html', {'form': form, 'problem': True, 'googlekey': googleKey})