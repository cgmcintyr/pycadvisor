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

    def test_container_spec_container_spec(self):
        data = {'creation_time':'2016-08-24T21:19:24.623769018Z'}
        time = datetime(2016, 8, 24, 21, 19, 24, 623769)
        self.assertEqual(ContainerSpec(data).creation_time, time)
