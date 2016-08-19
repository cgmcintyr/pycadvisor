# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import unittest
import json

import requests_mock

import cadvisor.tests.mocks as mocks
from cadvisor import Cadvisor
from cadvisor.info.v1.machine import MachineInfo
from cadvisor.info.v1.machine import FsInfo
from cadvisor.info.v1.machine import DiskInfo
from cadvisor.info.v1.machine import NetInfo
from cadvisor.info.v1.machine import Node
from cadvisor.info.v1.machine import Core
from cadvisor.info.v1.machine import Cache

class TestV1MachineInfo(unittest.TestCase):
    def test_machine_info_returns_machine_info_object(self):
        machine = MachineInfo({'num_cores': 'test'})
        self.assertEqual(machine.num_cores, 'test')

    def test_machine_info_cpu_frequency_khz(self):
        machine = MachineInfo({'cpu_frequency_khz': 'test'})
        self.assertEqual(machine.cpu_frequency_khz, 'test')

    def test_machine_info_machine_id(self):
        machine = MachineInfo({'machine_id': 'test'})
        self.assertEqual(machine.machine_id, 'test')

    def test_machine_info_boot_id(self):
        machine = MachineInfo({'boot_id': 'test'})
        self.assertEqual(machine.boot_id, 'test')

    def test_machine_info_cloud_provider(self):
        machine = MachineInfo({'cloud_provider': 'test'})
        self.assertEqual(machine.cloud_provider, 'test')

    def test_machine_info_instance_type(self):
        machine = MachineInfo({'instance_type': 'test'})
        self.assertEqual(machine.instance_type, 'test')

    def test_machine_info_instance_id(self):
        machine = MachineInfo({'instance_id': 'test'})
        self.assertEqual(machine.instance_id, 'test')

    def test_fs_info_device(self):
        fs = FsInfo({'device':'test'})
        self.assertEqual(fs.device, 'test')

    def test_fs_info_capacity(self):
        fs = FsInfo({'capacity':'test'})
        self.assertEqual(fs.capacity, 'test')

    def test_fs_info_fs_type(self):
        fs = FsInfo({'type': 'test'})
        self.assertEqual(fs.fs_type, 'test')

    def test_fs_info_has_inodes(self):
        fs = FsInfo({'has_inodes': 'test'})
        self.assertEqual(fs.has_inodes, 'test')

    def test_fs_info_inodes(self):
        fs = FsInfo({'inodes': 'test'})
        self.assertEqual(fs.inodes, 'test')

    def test_disk_info_name(self):
        disk = DiskInfo({'name':'test'})
        self.assertEqual(disk.name, 'test')

    def test_disk_info_major(self):
        disk = DiskInfo({'major':'test'})
        self.assertEqual(disk.major, 'test')

    def test_disk_info_minor(self):
        disk = DiskInfo({'minor':'test'})
        self.assertEqual(disk.minor, 'test')

    def test_disk_info_size(self):
        disk = DiskInfo({'size':'test'})
        self.assertEqual(disk.size, 'test')

    def test_disk_info_scheduler(self):
        disk = DiskInfo({'scheduler':'test'})
        self.assertEqual(disk.scheduler, 'test')

    def test_net_info_name(self):
        net = NetInfo({'name':'test'})
        self.assertEqual(net.name, 'test')

    def test_net_info_mac_address(self):
        net = NetInfo({'mac_address':'test'})
        self.assertEqual(net.mac_address, 'test')

    def test_net_info_speed(self):
        net = NetInfo({'speed':'test'})
        self.assertEqual(net.speed, 'test')

    def test_net(self):
        net = NetInfo({'mtu':'test'})
        self.assertEqual(net.mtu, 'test')

    def test_node_node_id(self):
        node = Node({'node_id':'test'})
        self.assertEqual(node.node_id, 'test')

    def test_node_memory(self):
        node = Node({'memory':'test'})
        self.assertEqual(node.memory, 'test')

    def test_core_core_id(self):
        core = Core({'core_id':'test'})
        self.assertEqual(core.core_id, 'test')

    def test_core_threads(self):
        core = Core({'thread_ids':'test'})
        self.assertEqual(core.threads, 'test')

    def test_cache_size(self):
        cache = Cache({'size':'test'})
        self.assertEqual(cache.size, 'test')

    def test_cache_cache_type(self):
        cache = Cache({'type':'test'})
        self.assertEqual(cache.cache_type, 'test')

    def test_cache_level(self):
        cache = Cache({'level':'test'})
        self.assertEqual(cache.level, 'test')

    def test_filesystems_creates_list(self):
        machine = MachineInfo({'filesystems':[{'device':'test'},{'device':'test'}]})
        self.assertEqual(len(machine.filesystems), 2)
        self.assertTrue(all(isinstance(x, FsInfo) for x in machine.filesystems))

    def test_filesystems_list_of_correct_type(self):
        machine = MachineInfo({'filesystems':[{'device':'test'},{'device':'test'}]})
        self.assertTrue(all(isinstance(x, FsInfo) for x in machine.filesystems))
    def test_disk_map_creates_list(self):
        machine = MachineInfo({'disk_map':[{'name':'test'},{'name':'test'}]})
        self.assertEqual(len(machine.disk_map), 2)

    def test_disk_map_list_of_correct_type(self):
        machine = MachineInfo({'disk_map':[{'name':'test'},{'name':'test'}]})
        self.assertTrue(all(isinstance(x, DiskInfo) for x in machine.disk_map))

    def test_network_devices_creates_list(self):
        machine = MachineInfo({'network_devices':[{'name':'test'},{'name':'test'}]})
        self.assertEqual(len(machine.network_devices), 2)

    def test_network_devices_list_of_correct_type(self):
        machine = MachineInfo({'network_devices':[{'name':'test'},{'name':'test'}]})
        self.assertTrue(all(isinstance(x, NetInfo) for x in machine.network_devices))

    def test_topology_creates_list(self):
        machine = MachineInfo({'topology':[{'node_id':'test'},{'node_id':'test'}]})
        self.assertEqual(len(machine.topology), 2)

    def test_topology_list_of_correct_type(self):
        machine = MachineInfo({'topology':[{'node_id':'test'},{'node_id':'test'}]})
        self.assertTrue(all(isinstance(x, Node) for x in machine.topology))

    def test_node_filesystems_list_of_correct_type(self):
        node = Node({'filesystems':[{'device':'test'},{'device':'test'}]})
        self.assertTrue(all(isinstance(x, FsInfo) for x in node.filesystems))

    def test_node_caches_creates_list(self):
        node = Node({'caches':[{'size':'test'},{'size':'test'}]})
        self.assertEqual(len(node.caches), 2)

    def test_node_caches_list_of_correct_type(self):
        node = Node({'caches':[{'size':'test'},{'size':'test'}]})
        self.assertTrue(all(isinstance(x, Cache) for x in node.caches))

    def test_node_cores_creates_list(self):
        node = Node({'cores':[{'core_id':'test'},{'core_id':'test'}]})
        self.assertEqual(len(node.cores), 2)

    def test_node_cores_list_of_correct_type(self):
        node = Node({'cores':[{'core_id':'test'},{'core_id':'test'}]})
        self.assertTrue(all(isinstance(x, Core) for x in node.cores))

    def test_core_caches_creates_list(self):
        core = Node({'caches':[{'size':'test'},{'size':'test'}]})
        self.assertEqual(len(core.caches), 2)

    def test_core_caches_list_of_correct_type(self):
        core = Node({'caches':[{'size':'test'},{'size':'test'}]})
        self.assertTrue(all(isinstance(x, Cache) for x in core.caches))

#    def test_create_object_on_none(self):
#        self.assertEqual(create_object_list(FsInfo, None), [])
#
#    def test_create_empty_list_on_none_object_list(self):
#        self.assertEqual(create_object_list(FsInfo, [None, None]), [])
