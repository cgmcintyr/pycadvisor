# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import requests

import cadvisor.api as api
from cadvisor.info.v1.machine import MachineInfo
from cadvisor.info.v1.container import ContainerInfo

class Cadvisor(object):
    API = 'api/v{}/'

    def __init__(self, url, version):
        if not url.endswith('/'): url+='/'
        self.base_url = url
        self.__validate_api_version(version)
        self.api_url = self.base_url + self.API.format(version)

    @staticmethod
    def __validate_api_version(version):
        if version not in api.SUPPORTED_VERSIONS:
            m = 'Invalid api version number \'{}\'. Supported api versions: {}'
            raise ValueError(m.format(version, api.SUPPORTED_VERSIONS))

    def get_all_info(self):
        return api.get_json_data(api.all_info_url(self.api_url))

    def get_machine_info(self):
        data = api.get_json_data(api.machine_info_url(self.api_url))
        return MachineInfo(data)

    def get_containers_info(self, name):
        data = api.get_json_data(api.containers_info_url(self.api_url, name))
        return ContainerInfo(data)

    def get_subcontainers_info(self, name):
        data = api.get_json_data(api.subcontainers_info_url(self.api_url, name))
        return [ContainerInfo(container) for container in data]

    def get_docker_container_info(self, name):
        data = api.get_json_data(api.docker_info_url(self.api_url, name))
        return ContainerInfo(data)

    def get_all_docker_containers_info(self):
        data = api.get_json_data(api.docker_info_url(self.api_url, ''))
        return [ContainerInfo(container) for container in data]
