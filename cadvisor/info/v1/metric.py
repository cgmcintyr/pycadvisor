# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from cadvisor.info.info import Info

class MetricSpec(Info):
    def setup(self):
        self.load_attr('name')
        self.load_attr('type')
        self.load_attr('format')
        self.load_attr('units')
