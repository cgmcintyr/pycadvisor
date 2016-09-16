# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from cadvisor.info.info import Info

class DockerStatus(Info):
    def _setup(self):
        self._load_attr('version')
        self._load_attr('kernel_version')
        self._load_attr('os')
        self._load_attr('hostname')
        self._load_attr('root_dir')
        self._load_attr('driver')
        self._load_attr('driver_status')
        self._load_attr('exec_driver')
        self._load_attr('num_images')
        self._load_attr('num_containers')

class DockerImage(Info):
    def _setup(self):
        self._load_attr('id')
        self._load_attr('repo_tags')
        self._load_attr('created')
        self._load_attr('virtual_size')
        self._load_attr('size')
