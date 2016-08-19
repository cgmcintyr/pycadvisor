# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import unittest
import json

import requests_mock

from cadvisor.info.info import Info

class TestInfo(unittest.TestCase):
    def test_create_object_on_none(self):
        info = Info({'test': None})
        info.load_attr_object_list('test', Info)
        self.assertEqual(info.test, [])

    def test_create_empty_list_on_none_object_list(self):
        info = Info({'test': [None, None]})
        info.load_attr_object_list('test', Info)
        self.assertEqual(info.test, [])
