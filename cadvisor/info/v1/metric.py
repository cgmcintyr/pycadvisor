# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from cadvisor.info.info import Info

class MetricSpec(Info):
    def _setup(self):
        self._load_attr('name')
        self._load_attr('type')
        self._load_attr('format')
        self._load_attr('units')

class MetricVal(Info):
    def _setup(self):
        self._load_attr('label')
        self._load_attr('timestamp')
        self._load_attr('int_value')
        self._load_attr('float_value')
