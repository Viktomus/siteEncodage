from urllib.request import urlopen
from chardet.universaldetector import UniversalDetector

def getFileEncoding(file):
    print(type(file))
    detector = UniversalDetector()
    detector.feed(file.read())
    detector.close()
    return detector.result['encoding']