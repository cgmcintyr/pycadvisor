# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from cadvisor.info.info import Info

class ContainerInfo(Info):
    def __init__(self, dictionary):
        Info.__init__(self, dictionary)

    def setup(self):
        # Container Reference
        self.load_attr('id', attr='container_id')
        self.load_attr('name')
        self.load_attr('aliases')
        self.load_attr('namespace')
        self.load_attr('labels')
