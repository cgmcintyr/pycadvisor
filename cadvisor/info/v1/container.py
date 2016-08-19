# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

class ContainerInfo:
    def __init__(self, dictionary):
        self.data = dictionary
        self.set_attr_from_dict('id', attr='container_id')
        self.set_attr_from_dict('name')
        self.set_attr_from_dict('aliases')
        self.set_attr_from_dict('namespace')
        self.set_attr_from_dict('labels')

    def set_attr_from_dict(self, key, attr=None):
        value = self.data.get(key)
        if attr is None: attr=key
        setattr(self, attr, value)
