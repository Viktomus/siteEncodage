from urllib.request import urlopen
from chardet.universaldetector import UniversalDetector
import os
import sys

notAllowedExt = ['.zip', '.rar', '.dll', '.exe', '.pdf']
#0=o, 1=Ko, 2=Mo, 3=Go

def getFileSizeUnit(size):
    unit = 0
    koSize = 1000
    moSize = 1000000
    goSize = 1000000000

    if size >= koSize and size < moSize:
        unit = 1
        size /= koSize
    elif size >= moSize and size < goSize:
        unit = 2
        size /= moSize
    elif size >= goSize:
        unit = 3
        size /= goSize
    size = int(size)
    return size,unit

def getUnitFromInt(unit):
    if unit == 0:
        return 'o'
    elif unit == 1:
        return 'Ko'
    elif unit == 2:
        return 'Mo'
    else:
        return 'Go'

def getFileExtension(fileName):
    fileName, file_extension = os.path.splitext(fileName)
    return file_extension

def isExtensionAuthorised(fileExt):
    for ext in notAllowedExt:
        if ext == fileExt:
            return False
    return True

def getFileEncoding(file):
    if isExtensionAuthorised(getFileExtension(file.name)) == False:
        return "","Fichier non supporté !"
    try:   
        detector = UniversalDetector()
        detector.feed(file.read())
        detector.close()
    except:
        return "","Fichier corrompu !"
    return detector.result['encoding'],""

def changeFileEncoding(file,currentEncoding,newEncoding):#Ne marche pas
    try:
        path = getLocalFilePath(file)

        f= open(path, 'rb')
        ts = f.read().decode(currentEncoding)
        es = ts.encode(newEncoding) 
        f= open(path,'wb')
        f.write(es) 
    except Exception as e:
        return e

    return ''

def getFilePath(file):
    return 'files/files/' + file.name

def getLocalFilePath(file):
    return 'media/files/' + file.name

def checkCaptcha(request):
    return ''
