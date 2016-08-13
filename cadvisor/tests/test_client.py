# -*- coding: utf-8 -*-

import unittest

from cadvisor import Cadvisor
from cadvisor.info.v1.machine import MachineInfo

class TestClient(unittest.TestCase):

    def setUp(self):
        self.url = 'url/'
        self.container_name = 'name'
        self.c = Cadvisor(self.url)

    def test_cadvisor_initializes_with_base_url_ending_in_forward_slash(self):
        self.assertEqual(self.c.baseUrl(), self.url)

    def test_cadvisor_initializes_with_base_url_not_ending_in_forward_slash(self):
        self.c = Cadvisor('url')
        self.assertEqual(self.c.baseUrl(), 'url' + '/')

    def test_cadvisor_machine_info_url(self):
        machineInfo = self.c.machineInfoUrl()
        self.assertEqual(machineInfo, self.url + 'machine')

    def test_cadvisor_all_info_url(self):
        allInfo = self.c.allInfoUrl()
        self.assertEqual(allInfo, self.url)

    def test_cadvisor_docker_info_url(self):
        dockerInfo = self.c.dockerInfoUrl(self.container_name)
        self.assertEqual(dockerInfo, self.url + 'docker/' + self.container_name)

    def test_cadvisor_containers_info_url(self):
        containersInfo = self.c.containersInfoUrl(self.container_name)
        self.assertEqual(containersInfo, self.url + 'containers/' + self.container_name)

    def test_cadvisor_subcontainers_info_url(self):
        subcontainersInfo = self.c.subcontainersInfoUrl(self.container_name)
        self.assertEqual(subcontainersInfo, self.url + 'subcontainers/' + self.container_name)

    def test_cadvisor_events_info_url(self):
        eventsInfo = self.c.eventsInfoUrl(self.container_name)
        self.assertEqual(eventsInfo, self.url + 'events/' + self.container_name)

if __name__ == '__main__':
    unittest.main()
