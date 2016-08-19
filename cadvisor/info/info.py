# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

class Info:
    "Parent class for info objects"

    def __init__(self, dictionary):
        self._data = dictionary

    def load_attr(self, key, attr=None):
        if attr is None: attr=key
        setattr(self, attr, self._data.get(key))
