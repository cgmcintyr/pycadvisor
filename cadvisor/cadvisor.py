# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import requests

import cadvisor.api as api
from cadvisor.info.v1.machine import MachineInfo
from cadvisor.info.v1.container import ContainerInfo

class Cadvisor(object):
    def __init__(self, url):
        if not url.endswith('/'): url+='/'
        self.base_url = url

    def get_all_info(self):
        return api.get_json_data(api.all_info_url(self.base_url))

    def get_machine_info(self):
        data = api.get_json_data(api.machine_info_url(self.base_url))
        return MachineInfo(data)

    def get_containers_info(self, name):
        data = api.get_json_data(api.containers_info_url(self.base_url, name))
        return ContainerInfo(data)
