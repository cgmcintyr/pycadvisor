# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from datetime import datetime

from cadvisor.info.info import Info
from cadvisor.info.v1.metric import MetricSpec

class ContainerSpec(Info):
    def __init__(self, dictionary, **kwargs):
        Info.__init__(self, dictionary, **kwargs)

    def setup(self):
        self.load_attr('creation_time', convert=self.__to_datetime)

        self.load_attr('labels')
        self.load_attr('envs')

        self.load_attr('has_cpu')
        self.load_attr_info('cpu', CpuSpec)

        self.load_attr('has_memory')
        self.load_attr_info('memory', MemorySpec)

        self.load_attr('has_network')
        self.load_attr('has_filesystem')
        self.load_attr('has_diskio')

        self.load_attr('has_custom_metrics')
        self.load_attr_info_list('custom_metrics', MetricSpec)

    @staticmethod
    def __to_datetime(value):
        go_time_format = '%Y-%m-%dT%H:%M:%S.%f'
        return datetime.strptime(value[:-4], go_time_format)

class CpuSpec(Info):
    def setup(self):
        self.load_attr('limit')
        self.load_attr('max_limit')
        self.load_attr('mask')
        self.load_attr('quota')
        self.load_attr('period')

class MemorySpec(Info):
    def setup(self):
        self.load_attr('limit')
        self.load_attr('reservation')
        self.load_attr('swap_limit')