import requests

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

def all_info_url(base_url):
    return base_url

def machine_info_url(base_url):
    return urljoin(base_url, 'machine')

def containers_info_url(base_url, name):
    return urljoin(base_url, 'containers/' +  name)

def subcontainers_info_url(base_url, name):
    return urljoin(base_url, 'subcontainers/' + name)

def docker_info_url(base_url, name):
    return urljoin(base_url, 'docker/' + name)

def events_info_url(base_url, name):
    return urljoin(base_url, 'events/' + name)

def get_json_data(url):
    r = requests.get(url).json()
    return r.json()

