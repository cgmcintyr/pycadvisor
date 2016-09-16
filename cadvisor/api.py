import requests

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

SUPPORTED_VERSIONS = ['1.0', '1.1', '1.2', '1.3']

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
