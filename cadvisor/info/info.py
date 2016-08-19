# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

class Info:
    "Parent class for info objects"

    def __init__(self, dictionary):
        self._data = dictionary

    def load_attr(self, key, attr=None):
        if attr is None: attr=key
        setattr(self, attr, self._data.get(key))

    def load_attr_object_list(self, key, cls, attr=None):
        if attr is None: attr=key
        setattr(self, attr, [])

        obj_list = self._data.get(key)
        if obj_list:
            setattr(self, attr, [cls(d) for d in obj_list if d is not None])
