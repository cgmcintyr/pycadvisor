# -*- coding: utf-8 -*-

import unittest
from cadvisor import api

class TestApi(unittest.TestCase):

    def setUp(self):
        self.url = 'url/'
        self.container_name = 'name'

    def test_cadvisor_machine_info_url(self):
        machine_info = api.machine_info_url(self.url)
        self.assertEqual(machine_info, self.url + 'machine')

    def test_cadvisor_all_info_url(self):
        all_info = api.all_info_url(self.url)
        self.assertEqual(all_info, self.url)

    def test_cadvisor_docker_info_url(self):
        docker_info = api.docker_info_url(self.url, self.container_name)
        self.assertEqual(docker_info, self.url + 'docker/' + self.container_name)

    def test_cadvisor_containers_info_url(self):
        containers_info = api.containers_info_url(self.url, self.container_name)
        self.assertEqual(containers_info, self.url + 'containers/' + self.container_name)

    def test_cadvisor_subcontainers_info_url(self):
        subcontainers_info = api.subcontainers_info_url(self.url, self.container_name)
        self.assertEqual(subcontainers_info, self.url + 'subcontainers/' + self.container_name)

    def test_cadvisor_events_info_url(self):
        events_info = api.events_info_url(self.url, self.container_name)
        self.assertEqual(events_info, self.url + 'events/' + self.container_name)

if __name__ == '__main__':
    unittest.main()
