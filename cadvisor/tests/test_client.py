# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import unittest
import json

import requests_mock

import cadvisor.tests.mocks as mocks
from cadvisor import Cadvisor
from cadvisor.info.v1.machine import MachineInfo
from cadvisor.info.v1.container import ContainerInfo

class TestClient(unittest.TestCase):

    URL = 'http://testurl.com/'

    def setUp(self):
        self.container_name = 'name'
        self.c = Cadvisor(TestClient.URL)

    def test_cadvisor_initializes_with_base_url_ending_in_forward_slash(self):
        self.assertEqual(self.c.base_url, TestClient.URL)

    def test_cadvisor_initializes_with_base_url_not_ending_in_forward_slash(self):
        url = 'http://url'
        self.c = Cadvisor(url)
        self.assertEqual(self.c.base_url, url + '/')

    def test_get_machine_info_returns_machine_info_object(self):
        with requests_mock.mock() as m:
            m.get('http://testurl.com/machine', text='{}', status_code=200)
            machine = self.c.get_machine_info()
            self.assertIsInstance(machine, MachineInfo)

    def test_get_containers_info_returns_container_info_object(self):
        with requests_mock.mock() as m:
            m.get('http://testurl.com/containers/test',text='{}', status_code=200)
            container = self.c.get_containers_info('test')
            self.assertIsInstance(container, ContainerInfo)

