# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import unittest

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

    def test__load_attr(self):
        info = Info({'test': 'test'}, preserve_data=True)
        info._load_attr('test')
        self.assertEqual(info.test, 'test')

    def test__load_attr_on_missing_key(self):
        info = Info({}, preserve_data=True)
        info._load_attr('test')
        self.assertEqual(info.test, None)

    def test_subscriptable(self):
        info = Info({})
        setattr(info, 'test', 1)
        self.assertEqual(info['test'], 1)

    def test__load_attr_on_invalid_name(self):
        info = Info({'1': 1}, preserve_data=True)
        info._load_attr('1')
        self.assertEqual(info['1'], 1)

    def test__load_attr_twice(self):
        info = Info({'1': 1}, preserve_data=True)
        with self.assertRaises(AttributeError):
            info._load_attr('1')
            info._load_attr('1')

    def test__load_attr_as(self):
        info = Info({'subinfo': {'test':True}}, preserve_data=True)
        info._load_attr_as('subinfo', Info, preserve_data=True)
        info.subinfo._load_attr('test')
        self.assertEqual(info.subinfo.test, True)

    def test__load_attr_as_on_none(self):
        info = Info({'test': None}, preserve_data=True)
        info._load_attr_as('test', Info)
        self.assertEqual(info.test, None)

    def test__load_attr_as_list_of_on_none(self):
        info = Info({'test': None}, preserve_data=True)
        info._load_attr_as_list_of('test', Info)
        self.assertEqual(info.test, [])

    def test__load_attr_as_list_of_on_list_of_none(self):
        with self.assertRaises(TypeError):
            info = Info({'sub_info_data': [None, None]}, preserve_data=True)
            info._load_attr_as_list_of('sub_info_data', Info)

    def test__load_attr_as_list_of_on_list_mixed_none(self):
        with self.assertRaises(TypeError):
            info = Info({'sub_info_data': [None, {'test':'test'}]}, preserve_data=True)
            info._load_attr_as_list_of('sub_info_data', Info)

    def test__load_attr_as_list_of_on_string(self):
        with self.assertRaises(TypeError):
            info = Info({'sub_info_data': 'test'}, preserve_data=True)
            info._load_attr_as_list_of('sub_info_data', Info)
