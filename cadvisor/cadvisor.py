# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import json
import requests

import cadvisor.api as api
from cadvisor.info.v1.machine import MachineInfo
from cadvisor.info.v1.container import ContainerInfo
from cadvisor.info.v1.container.event import Event

class Cadvisor(object):
    API = 'api/v{}/'

    def __init__(self, url, version):
        if not url.endswith('/'): url+='/'
        self.base_url = url
        self.__validate_api_version(version)
        self.api_url = self.base_url + self.API.format(version)

    @staticmethod
    def __get_json_data(url):
        return requests.get(url).json()

    @staticmethod
    def __get_events_stream(url):
        resp = requests.get(url, stream=True)
        for line in resp.iter_lines():
            if line:
                data = json.loads(line)
                yield Event(data)

    @staticmethod
    def __validate_api_version(version):
        if version not in api.SUPPORTED_VERSIONS:
            m = 'Invalid api version number \'{}\'. Supported api versions: {}'
            raise ValueError(m.format(version, api.SUPPORTED_VERSIONS))

    def get_all_info(self):
        return self.__get_json_data(api.all_info_url(self.api_url))

    def get_machine_info(self):
        data = self.__get_json_data(api.machine_info_url(self.api_url))
        return MachineInfo(data)

    def get_containers_info(self, name):
        data = self.__get_json_data(api.containers_info_url(self.api_url, name))
        return ContainerInfo(data)

    def get_subcontainers_info(self, name):
        data = self.__get_json_data(api.subcontainers_info_url(self.api_url, name))
        return [ContainerInfo(container) for container in data]

    def get_docker_container_info(self, name):
        data = self.__get_json_data(api.docker_info_url(self.api_url, name))
        return ContainerInfo(data)

    def get_all_docker_containers_info(self):
        data = self.__get_json_data(api.docker_info_url(self.api_url, ''))
        return [ContainerInfo(container) for container in data]

    def get_event_static_info(self, name):
        data = self.__get_json_data(api.events_info_url(self.api_url, name))
        return [Event(event) for event in data]

    def get_event_streaming_info(self, name):
        return self.__get_events_stream(api.events_info_url(self.api_url, name))
