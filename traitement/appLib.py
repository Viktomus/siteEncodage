from urllib.request import urlopen
from chardet.universaldetector import UniversalDetector
import os
import sys

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

def getFileEncoding(file):
    try:   
        detector = UniversalDetector()
        detector.feed(file.read())
        detector.close()
    except:
        return "","Fichier illisible !"
    return detector.result['encoding'],""

def getWebAddress(request,replacement='index'):
    address = request.build_absolute_uri()
    return address.replace(replacement,'')