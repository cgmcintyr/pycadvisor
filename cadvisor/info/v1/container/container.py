# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from datetime import datetime

from cadvisor.info.info import Info
from cadvisor.info.v1.container.spec import ContainerSpec
from cadvisor.info.v1.container.stats import ContainerStats
from cadvisor.info.v1.metric import MetricSpec, MetricVal

class ContainerInfo(Info):
    def setup(self):
        self.reference = ContainerReference(self._data, parent=self)
        self.load_attr_info_list('subcontainers', ContainerReference)
        self.load_attr_info('spec', ContainerSpec)
        self.load_attr_info_list('stats', ContainerStats)

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
