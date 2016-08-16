import requests

from . import api

class Cadvisor(object):
    def __init__(self, url):
        if not url.endswith('/'): url+='/'
        self.base_url = url

    def get_all_info(self):
        return api.get_json_data(api.all_info_url(self.base_url))

    def get_machine_info(self):
        return api.get_json_data(api.machine_info_url(self.base_url))
