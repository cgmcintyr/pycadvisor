# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import unittest
import json

from datetime import datetime

import requests_mock

import cadvisor.tests.mocks as mocks
from cadvisor.info.v1.container import ContainerInfo
from cadvisor.info.v1.container import ContainerReference
from cadvisor.info.v1.container import ContainerSpec
from cadvisor.info.v1.container import CpuSpec
from cadvisor.info.v1.container import MemorySpec
from cadvisor.info.v1.container import MetricSpec

class TestV1ContainerInfo(unittest.TestCase):
    def test_init_id(self):
        container = ContainerInfo({'id': 'test'})
        self.assertEqual(container.container_id, 'test')

    def test_init_name(self):
        container = ContainerInfo({'name': 'test'})
        self.assertEqual(container.name, 'test')

    def test_init_aliases(self):
        container = ContainerInfo({'aliases':'test'})
        self.assertEqual(container.aliases, 'test')

    def test_init_namespace(self):
        container = ContainerInfo({'namespace':['test', 'test2']})
        self.assertEqual(container.namespace, ['test', 'test2'])

    def test_init_labels(self):
        container = ContainerInfo({'labels':{'test':'label', 'test2':'label2'}})
        self.assertEqual(container.labels, {'test':'label', 'test2':'label2'})

    def test_init_embedded_reference_parent(self):
        container = ContainerInfo({})
        self.assertEqual(container.reference.parent, container)

    def test_init_embedded_reference_id(self):
        container = ContainerInfo({'id': 'test'})
        self.assertEqual(container.reference.container_id, 'test')

    def test_init_embedded_reference_name(self):
        container = ContainerInfo({'name': 'test'})
        self.assertEqual(container.reference.name, 'test')

    def test_init_embedded_reference_aliases(self):
        container = ContainerInfo({'aliases':'test'})
        self.assertEqual(container.reference.aliases, 'test')

    def test_init_embedded_reference_namespace(self):
        container = ContainerInfo({'namespace':['test', 'test2']})
        self.assertEqual(container.reference.namespace, ['test', 'test2'])

    def test_init_embedded_reference_labels(self):
        container = ContainerInfo({'labels':{'test':'label', 'test2':'label2'}})
        self.assertEqual(container.reference.labels, {'test':'label', 'test2':'label2'})

    def test_init_subcontainers(self):
        container = ContainerInfo({'subcontainers': [{'id': 'test'}, {'id':'test2'}]})
        self.assertEqual(len(container.subcontainers), 2)
        self.assertEqual(container.subcontainers[0].container_id, 'test')
        self.assertEqual(container.subcontainers[1].container_id, 'test2')

    def test_init_container_reference_with_invalid_parent(self):
        with self.assertRaises(TypeError):
            class Object(object):
                pass
            ContainerReference({'id':'test'}, parent=Object())

    def test_init_container_reference_parent_defaults_none(self):
        self.assertEqual(ContainerReference({}).parent, None)

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

    def test_metric_spec_creates_list(self):
        container = ContainerSpec({'custom_metrics':[{'name':'test'},{'name':'test'}]})
        self.assertEqual(len(container.custom_metrics), 2)
        self.assertTrue(all(isinstance(x, MetricSpec) for x in container.custom_metrics))

    def test_metric_spec_list_of_correct_type(self):
        machine = ContainerSpec({'custom_metrics':[{'name':'test'},{'name':'test'}]})
        self.assertTrue(all(isinstance(x, MetricSpec) for x in machine.custom_metrics))

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

    def test_init_memory_spec_limit(self):
        self.assertEqual(MemorySpec({'limit':True}).limit, True)

    def test_init_memory_spec_reservation(self):
        self.assertEqual(MemorySpec({'reservation':True}).reservation, True)

    def test_init_memory_spec_swap_limit(self):
        self.assertEqual(MemorySpec({'swap_limit':True}).swap_limit, True)

    def test_init_metric_spec_name(self):
        self.assertEqual(MetricSpec({'name':True}).name, True)

    def test_init_metric_spec_type(self):
        self.assertEqual(MetricSpec({'type':True}).type, True)

    def test_init_metric_spec_format(self):
        self.assertEqual(MetricSpec({'format':True}).format, True)

    def test_init_metric_spec_units(self):
        self.assertEqual(MetricSpec({'units':True}).units, True)
