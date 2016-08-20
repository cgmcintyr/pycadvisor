# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from collections import namedtuple

from cadvisor.info.info import Info

class ContainerInfo(Info):
    def __init__(self, dictionary, **kwargs):
        Info.__init__(self, dictionary, **kwargs)

    def setup(self):
        # Container Reference
        self.load_attr('id', attr='container_id')
        self.load_attr('name')
        self.load_attr('aliases')
        self.load_attr('namespace')
        self.load_attr('labels')

ContainerReference = namedtuple('ContainerReference',
                                'name id aliases namespace labels')
ContainerReference.__new__.__defaults__ = (None,) * (len(ContainerReference._fields) - 1)
