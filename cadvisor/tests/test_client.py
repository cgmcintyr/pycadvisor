# -*- coding: utf-8 -*-

import unittest
import json

import requests_mock

from cadvisor import Cadvisor
import cadvisor.tests.mocks as mocks

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

    def test_machine_info_returns_json(self):
        with requests_mock.mock() as m:
            m.get(requests_mock.ANY, text=mocks.machine_info_1)
            self.assertEqual(self.c.get_machine_info(), json.loads(mocks.machine_info_1))


if __name__ == '__main__':
    unittest.main()
