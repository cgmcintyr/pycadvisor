# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from collections import namedtuple
from datetime import datetime

from cadvisor.info.info import Info

class ContainerInfo(Info):
    def setup(self):
        self.reference = ContainerReference(self._data, parent=self)
        self.load_attr_info_list('subcontainers', ContainerReference)

class ContainerReference(Info):
    def __init__(self, dictionary, parent=None, **kwargs):
        if self.__validate_parent(parent): self.parent = parent
        Info.__init__(self, dictionary, **kwargs)

    def setup(self):
        self.load_attr('id', attr='container_id')
        self.load_attr('name')
        self.load_attr('aliases')
        self.load_attr('namespace')
        self.load_attr('labels')

        if self.parent:
            for k, v in vars(self).items():
                if not k.startswith('_'):
                    setattr(self.parent, k, v)

    def __validate_parent(self, parent):
        if parent is None:
            pass
        elif parent.__class__ is not ContainerInfo:
            msg = 'parent must have type None or be an instance of ContainerInfo'
            raise TypeError(msg)
        return True

class ContainerSpec(Info):
    def __init__(self, dictionary, **kwargs):
        Info.__init__(self, dictionary, **kwargs)

    def setup(self):
        self.load_attr('creation_time', convert=self.__to_datetime)

        self.load_attr('labels')
        self.load_attr('envs')

        self.load_attr('has_cpu')
        self.load_attr('cpu', convert=self.__to_cpuspec)

        self.load_attr('has_memory')
        self.load_attr('memory', convert=self.__to_memoryspec)

        self.load_attr('has_network')
        self.load_attr('has_filesystem')
        self.load_attr('has_diskio')

        self.load_attr('has_custom_metrics')
        self.load_attr_info_list('custom_metrics', MetricSpec)

    @staticmethod
    def __to_datetime(value):
        go_time_format = '%Y-%m-%dT%H:%M:%S.%f'
        return datetime.strptime(value[:-4], go_time_format)

    @staticmethod
    def __to_cpuspec(value):
        return CpuSpec(value)

    @staticmethod
    def __to_memoryspec(value):
        return MemorySpec(value)

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

class MetricSpec(Info):
    def setup(self):
        self.load_attr('name')
        self.load_attr('type')
        self.load_attr('format')
        self.load_attr('units')
