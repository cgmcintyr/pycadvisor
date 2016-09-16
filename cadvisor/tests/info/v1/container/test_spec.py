# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import unittest

from datetime import datetime

from cadvisor.info.v1.container.spec import ContainerSpec
from cadvisor.info.v1.container.spec import CpuSpec
from cadvisor.info.v1.container.spec import MemorySpec
from cadvisor.info.v1.metric import MetricSpec

class TestV1ContainerInfo(unittest.TestCase):
    def test_init_container_spec_creation_time(self):
        data = {'creation_time':'2016-08-24T21:19:24.623769018Z'}
        time = datetime(2016, 8, 24, 21, 19, 24, 623769)
        self.assertEqual(ContainerSpec(data).creation_time, time)

    def test_init_container_spec_labels(self):
        labels = {'test':'test', 'test2':'test2'}
        spec = ContainerSpec({'labels':labels})
        self.assertEqual(spec.labels, labels)

    def test_init_container_spec_envs(self):
        envs = {'test':'test', 'test2':'test2'}
        spec = ContainerSpec({'envs':envs})
        self.assertEqual(spec.envs, envs)

    def test_init_container_spec_has_cpu(self):
        self.assertEqual(ContainerSpec({'has_cpu':True}).has_cpu, True)

    def test_init_container_spec_cpu(self):
        data = {'limit':12345}
        cpu = CpuSpec(data)
        container = ContainerSpec({'cpu':data})
        self.assertEqual(container.cpu.__class__, CpuSpec)
        self.assertEqual(container.cpu.limit, cpu.limit)

    def test_init_container_spec_has_memory(self):
        self.assertEqual(ContainerSpec({'has_memory':True}).has_memory, True)

    def test_init_container_spec_memory(self):
        data = {'reservation':12345}
        memory = MemorySpec(data)
        container = ContainerSpec({'memory':data})
        self.assertEqual(container.memory.__class__, MemorySpec)
        self.assertEqual(container.memory.reservation, memory.reservation)

    def test_init_container_spec_has_network(self):
        self.assertEqual(ContainerSpec({'has_network':True}).has_network, True)

    def test_init_container_spec_has_filesystem(self):
        self.assertEqual(ContainerSpec({'has_filesystem':True}).has_filesystem, True)

    def test_init_container_spec_has_diskio(self):
        self.assertEqual(ContainerSpec({'has_diskio':True}).has_diskio, True)

    def test_init_container_spec_has_custom_metrics(self):
        self.assertEqual(ContainerSpec({'has_custom_metrics':True}).has_custom_metrics, True)

    def test_init_container_spec_custom_metrics_creates_list(self):
        container = ContainerSpec({'custom_metrics':[{'name':'test'},{'name':'test'}]})
        self.assertEqual(len(container.custom_metrics), 2)

    def test_init_container_spec_custom_metrics_correct_type(self):
        machine = ContainerSpec({'custom_metrics':[{'name':'test'},{'name':'test'}]})
        self.assertTrue(all(isinstance(x, MetricSpec) for x in machine.custom_metrics))

class TestV1CpuSpec(unittest.TestCase):
    def test_init_cpu_spec_limit(self):
        self.assertEqual(CpuSpec({'limit':True}).limit, True)

    def test_init_cpu_spec_max_limit(self):
        self.assertEqual(CpuSpec({'max_limit':True}).max_limit, True)

    def test_init_cpu_spec_mask(self):
        self.assertEqual(CpuSpec({'mask': True}).mask, True)

    def test_init_cpu_spec_quota(self):
        self.assertEqual(CpuSpec({'quota':True}).quota, True)

    def test_init_cpu_spec_period(self):
        self.assertEqual(CpuSpec({'period':True}).period, True)

class TestV1MemorySpec(unittest.TestCase):
    def test_init_memory_spec_limit(self):
        self.assertEqual(MemorySpec({'limit':True}).limit, True)

    def test_init_memory_spec_reservation(self):
        self.assertEqual(MemorySpec({'reservation':True}).reservation, True)

    def test_init_memory_spec_swap_limit(self):
        self.assertEqual(MemorySpec({'swap_limit':True}).swap_limit, True)
