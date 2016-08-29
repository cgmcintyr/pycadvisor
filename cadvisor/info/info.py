# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

class Info:
    def __init__(self, dictionary, preserve_data=False, **kwargs):
        self._data = dictionary
        self.setup()
        if not preserve_data: self._post_init()
        object(**kwargs)

    def __getitem__(self, x):
        return getattr(self, x)

    def __setattr__(self, attr, value):
        if hasattr(self, attr):
            raise AttributeError('Attempted to alter read-only value')
        else:
            self.__dict__[attr] = value

    @staticmethod
    def validate_info_list(info_list):
        if not (type(info_list) is list and all(type(x) is dict for x in info_list)):
            raise TypeError('Object list must be list of dictionaries')

    def setup(self):
        return None

    def load_attr(self, key, attr=None, convert=None):
        if attr is None: attr=key
        value = self._data.get(key)

        if value and convert:
            value = convert(value)

        setattr(self, attr, value)
        return value

    def load_attr_info(self, key, info_cls, attr=None, preserve_data=False):
        if attr is None: attr=key
        value = self._data.get(key)

        if value:
            value = info_cls(value, preserve_data=preserve_data)

        setattr(self, attr, value)
        return value

    def load_attr_info_list(self, key, info_cls, attr=None, preserve_data=False):
        if attr is None: attr=key

        info_list = self._data.get(key)
        if info_list is None:
            info_list = []
        elif not (type(info_list) is list and all(type(x) is dict for x in info_list)):
            raise TypeError('Object list must be list of dictionaries')
        else:
            Info.validate_info_list(info_list)
            info_list = [info_cls(data, preserve_data=preserve_data)
                         for data in info_list if data is not None]
        setattr(self, attr, info_list)
        return info_list

    def _post_init(self):
        del self._data
