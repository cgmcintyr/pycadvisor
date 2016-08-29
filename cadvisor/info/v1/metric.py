# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from cadvisor.info.info import Info

class MetricSpec(Info):
    def setup(self):
        self.load_attr('name')
        self.load_attr('type')
        self.load_attr('format')
        self.load_attr('units')

class MetricVal(Info):
    def setup(self):
        self.load_attr('label')
        self.load_attr('timestamp')
        self.load_attr('int_value')
        self.load_attr('float_value')
