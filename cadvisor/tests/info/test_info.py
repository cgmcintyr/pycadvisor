# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import unittest
import json

import requests_mock

from cadvisor.info.info import Info

class TestInfo(unittest.TestCase):

    def test_data_deleted_by_default(self):
        info = Info({'test': None})
        with self.assertRaises(AttributeError):
            info._data

    def test_data_not_deleted_with_preserve_data(self):
        info = Info({'test': None}, preserve_data=True)
        self.assertEqual(info._data, {'test':None})

    def test_load_attr(self):
        info = Info({'test': 'test'}, preserve_data=True)
        info.load_attr('test')
        self.assertEqual(info.test, 'test')

    def test_load_attr_on_missing_key(self):
        info = Info({}, preserve_data=True)
        info.load_attr('test')
        self.assertEqual(info.test, None)

    def test_load_attr_on_invalid_name(self):
        info = Info({'1': 1}, preserve_data=True)
        info.load_attr('1')
        self.assertEqual(info['1'], 1)

    def test_load_attr_twice(self):
        info = Info({'1': 1}, preserve_data=True)
        with self.assertRaises(AttributeError):
            info.load_attr('1')
            info.load_attr('1')

    def test_load_attr_object_list_on_none(self):
        info = Info({'test': None}, preserve_data=True)
        info.load_attr_object_list('test', Info)
        self.assertEqual(info.test, [])

    def test_load_attr_object_list_on_list_of_none(self):
        info = Info({'sub_info_data': [None, None]}, preserve_data=True)
        info.load_attr_object_list('sub_info_data', Info)
        self.assertEqual(info.sub_info_data, [])

    def test_load_attr_object_list_on_list_mixed_none(self):
        info = Info({'sub_info_data': [None, {'test':'test'}]}, preserve_data=True)
        info.load_attr_object_list('sub_info_data', Info)
        self.assertEqual(len(info.sub_info_data), 1)
