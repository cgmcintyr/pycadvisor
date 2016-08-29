# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import unittest
import json

from cadvisor.info.v1.metric import MetricSpec

class TestV1MetricSpec(unittest.TestCase):
    def test_init_metric_spec_name(self):
        self.assertEqual(MetricSpec({'name':True}).name, True)

    def test_init_metric_spec_type(self):
        self.assertEqual(MetricSpec({'type':True}).type, True)

    def test_init_metric_spec_format(self):
        self.assertEqual(MetricSpec({'format':True}).format, True)

    def test_init_metric_spec_units(self):
        self.assertEqual(MetricSpec({'units':True}).units, True)
