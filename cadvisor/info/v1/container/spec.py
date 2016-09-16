# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from datetime import datetime

from cadvisor.info.info import Info
from cadvisor.info.v1.metric import MetricSpec

class ContainerSpec(Info):
    def __init__(self, dictionary, **kwargs):
        Info.__init__(self, dictionary, **kwargs)

    def _setup(self):
        self._load_attr('creation_time', convert=self.__to_datetime)

        self._load_attr('labels')
        self._load_attr('envs')

        self._load_attr('has_cpu')
        self._load_attr_as('cpu', CpuSpec)

        self._load_attr('has_memory')
        self._load_attr_as('memory', MemorySpec)

        self._load_attr('has_network')
        self._load_attr('has_filesystem')
        self._load_attr('has_diskio')

        self._load_attr('has_custom_metrics')
        self._load_attr_as_list_of('custom_metrics', MetricSpec)

    @staticmethod
    def __to_datetime(value):
        go_time_format = '%Y-%m-%dT%H:%M:%S.%f'
        return datetime.strptime(value[:-4], go_time_format)

class CpuSpec(Info):
    def _setup(self):
        self._load_attr('limit')
        self._load_attr('max_limit')
        self._load_attr('mask')
        self._load_attr('quota')
        self._load_attr('period')

class MemorySpec(Info):
    def _setup(self):
        self._load_attr('limit')
        self._load_attr('reservation')
        self._load_attr('swap_limit')
