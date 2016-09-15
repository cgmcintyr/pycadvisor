# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import unittest
import json

import requests_mock

import cadvisor.tests.mocks as mocks
from cadvisor import Cadvisor
from cadvisor.info.v1.machine import MachineInfo
from cadvisor.info.v1.container import ContainerInfo

class TestCadvisor(unittest.TestCase):

    URL = 'http://testurl.com/'
    API = '1.3'

    def setUp(self):
        self.container_name = 'name'
        self.c = Cadvisor(self.URL, self.API)

    def test_cadvisor_initializes_with_base_url_ending_in_forward_slash(self):
        self.assertEqual(self.c.base_url, self.URL)

    def test_cadvisor_initializes_with_base_url_not_ending_in_forward_slash(self):
        url = 'http://url'
        self.c = Cadvisor(url, self.API)
        self.assertEqual(self.c.base_url, url + '/')

    def test_get_machine_info_returns_machine_info_object(self):
        with requests_mock.mock() as m:
            url = '{}api/v{}/machine'.format(self.URL, self.API)
            m.get(url, text='{}', status_code=200)
            machine = self.c.get_machine_info()
            self.assertIsInstance(machine, MachineInfo)

    def test_get_containers_info_returns_container_info_object(self):
        with requests_mock.mock() as m:
            url = '{}api/v{}/containers/test'.format(self.URL, self.API)
            m.get(url, text='{}', status_code=200)
            container = self.c.get_containers_info('test')
            self.assertIsInstance(container, ContainerInfo)

    def test_get_subcontainers_info_returns_list_of_container_info_objects(self):
        with requests_mock.mock() as m:
            url = '{}api/v{}/subcontainers/test'.format(self.URL, self.API)
            m.get(url, text='[{}, {}]', status_code=200)
            subcontainers = self.c.get_subcontainers_info('test')
            self.assertIsInstance(subcontainers, list)
            self.assertTrue(all(isinstance(x, ContainerInfo) for x in subcontainers))

    def test_get_docker_container_info_returns_container_info_object(self):
        with requests_mock.mock() as m:
            url = '{}api/v{}/docker/test'.format(self.URL, self.API)
            m.get(url ,text='{}', status_code=200)
            docker = self.c.get_docker_container_info('test')
            self.assertIsInstance(docker, ContainerInfo)

    def test_get_all_docker_containers_info_returns_list_of_container_info_objects(self):
        with requests_mock.mock() as m:
            url = '{}api/v{}/docker/'.format(self.URL, self.API)
            m.get(url, text='[{}, {}]', status_code=200)
            docker = self.c.get_all_docker_containers_info()
            self.assertIsInstance(docker, list)
            self.assertTrue(all(isinstance(x, ContainerInfo) for x in docker))
