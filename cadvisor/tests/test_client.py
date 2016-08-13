# -*- coding: utf-8 -*-

import unittest

from cadvisor import Cadvisor

class TestClient(unittest.TestCase):

    def setUp(self):
        self.url = 'url/'
        self.container_name = 'name'
        self.c = Cadvisor(self.url)

    def test_cadvisor_initializes_with_base_url_ending_in_forward_slash(self):
        self.assertEqual(self.c.base_url, self.url)

    def test_cadvisor_initializes_with_base_url_not_ending_in_forward_slash(self):
        self.c = Cadvisor('url')
        self.assertEqual(self.c.base_url, 'url' + '/')

if __name__ == '__main__':
    unittest.main()
