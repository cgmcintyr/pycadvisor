# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from collections import namedtuple

from cadvisor.info.info import Info

class ContainerInfo(Info):
    def __init__(self, dictionary, **kwargs):
        Info.__init__(self, dictionary, **kwargs)

    def setup(self):
        self.reference = ContainerReference(self._data, parent=self)

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
        if parent.__class__ is not ContainerInfo:
            msg = 'parent must have type None or be an instance ofContainerInfo'
            raise TypeError(msg)
        return True
