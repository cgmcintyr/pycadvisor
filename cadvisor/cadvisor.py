import requests
import urlparse

class Cadvisor(object):
    def __init__(self, url):
        if not url.endswith('/'): url+='/'
        self._baseUrl = url

    def baseUrl(self):
        return self._baseUrl

    def allInfoUrl(self):
        return self._baseUrl

    def machineInfoUrl(self):
        return urlparse.urljoin(self._baseUrl, 'machine')

    def containersInfoUrl(self, name):
        return urlparse.urljoin(self._baseUrl, 'containers/' +  name)

    def subcontainersInfoUrl(self, name):
        return urlparse.urljoin(self._baseUrl, 'subcontainers/' + name)

    def dockerInfoUrl(self, name):
        return urlparse.urljoin(self._baseUrl, 'docker/' + name)

    def eventsInfoUrl(self, name):
        return  urlparse.urljoin(self._baseUrl, 'events/' + name)

    def getJsonData(url):
        r = requests.get(url).json()
        return r.json()
