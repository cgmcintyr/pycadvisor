# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import unittest
import json

from cadvisor.info.v1.docker import DockerStatus
from cadvisor.info.v1.docker import DockerImage

class TestV1DockerStatus(unittest.TestCase):
    def test_docker_status_version(self):
        status = DockerStatus({'version':'test'})
        self.assertEqual(status.version, 'test')

    def test_docker_status_kernel_version(self):
        status = DockerStatus({'kernel_version':'test'})
        self.assertEqual(status.kernel_version, 'test')

    def test_docker_status_os(self):
        status = DockerStatus({'os':'test'})
        self.assertEqual(status.os, 'test')

    def test_docker_status_hostname(self):
        status = DockerStatus({'hostname':'test'})
        self.assertEqual(status.hostname, 'test')

    def test_docker_status_root_dir(self):
        status = DockerStatus({'root_dir':'test'})
        self.assertEqual(status.root_dir, 'test')

    def test_docker_status_driver(self):
        status = DockerStatus({'driver':'test'})
        self.assertEqual(status.driver, 'test')

    def test_docker_status_driver_status(self):
        status = DockerStatus({'driver_status':'test'})
        self.assertEqual(status.driver_status, 'test')

    def test_docker_status_exec_driver(self):
        status = DockerStatus({'exec_driver':'test'})
        self.assertEqual(status.exec_driver, 'test')

    def test_docker_status_num_images(self):
        status = DockerStatus({'num_images':'test'})
        self.assertEqual(status.num_images, 'test')

    def test_docker_status_num_containers(self):
        status = DockerStatus({'num_containers':'test'})
        self.assertEqual(status.num_containers, 'test')


class TestV1DockerImage(unittest.TestCase):
    def test_docker_image_id(self):
        image = DockerImage({'id':'test'})
        self.assertEqual(image.id, 'test')

    def test_docker_image_repo_tags(self):
        image = DockerImage({'repo_tags':'test'})
        self.assertEqual(image.repo_tags, 'test')

    def test_docker_image_created(self):
        image = DockerImage({'created':'test'})
        self.assertEqual(image.created, 'test')

    def test_docker_image_virtual_size(self):
        image = DockerImage({'virtual_size':'test'})
        self.assertEqual(image.virtual_size, 'test')

    def test_docker_image_size(self):
        image = DockerImage({'size':'test'})
        self.assertEqual(image.size, 'test')
