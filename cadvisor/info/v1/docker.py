# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from cadvisor.info.info import Info

class DockerStatus(Info):
    def setup(self):
        self.load_attr('version')
        self.load_attr('kernel_version')
        self.load_attr('os')
        self.load_attr('hostname')
        self.load_attr('root_dir')
        self.load_attr('driver')
        self.load_attr('driver_status')
        self.load_attr('exec_driver')
        self.load_attr('num_images')
        self.load_attr('num_containers')

class DockerImage(Info):
    def setup(self):
        self.load_attr('id')
        self.load_attr('repo_tags')
        self.load_attr('created')
        self.load_attr('virtual_size')
        self.load_attr('size')
