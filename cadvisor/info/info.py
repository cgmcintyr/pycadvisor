# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

class Info:
    "Parent class for info objects"

    def __init__(self, dictionary, preserve_data=False, **kwargs):
        self._data = dictionary
        self.setup()
        if not preserve_data: self._post_init()
        object(**kwargs)

    def __getitem__(self, x):
        return getattr(self, x)

    def __setattr__(self, attr, value):
        if hasattr(self, attr): raise AttributeError('Attempting to alter read-only value')
        else: self.__dict__[attr] = value

    def setup(self):
        return None

    def _post_init(self):
        del self._data

    def load_attr(self, key, attr=None):
        if attr is None: attr=key
        setattr(self, attr, self._data.get(key))

    def load_attr_object_list(self, key, cls, attr=None, preserve_data=False):
        if attr is None: attr=key
        obj_list = self._data.get(key)
        if obj_list:
            obj_list = [cls(d, preserve_data=preserve_data) for d in obj_list
                        if d is not None]
        else:
            obj_list = []
        setattr(self, attr, obj_list)
