# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

class MachineInfo:
    def __init__(self, dictionary):
        self.num_cores = dictionary.get('num_cores')
        self.cpu_frequency_khz = dictionary.get('cpu_frequency_khz')
        self.machine_id = dictionary.get('machine_id')
        self.system_uuid = dictionary.get('system_uuid')
        self.boot_id = dictionary.get('boot_id')

        self.filesystems = create_object_list(FsInfo, dictionary.get('filesystems'))
        self.disk_map = create_object_list(DiskInfo, dictionary.get('disk_map'))
        self.network_devices = create_object_list(NetInfo, dictionary.get('network_devices'))
        self.topology = create_object_list(Node, dictionary.get('topology'))

        self.cloud_provider = dictionary.get('cloud_provider')
        self.instance_type = dictionary.get('instance_type')
        self.instance_id = dictionary.get('instance_id')

class FsInfo:
    def __init__(self, dictionary):
        self.device = dictionary.get('device')
        self.capacity = dictionary.get('capacity')
        self.fs_type = dictionary.get('type')
        self.has_inodes = dictionary.get('has_inodes')
        self.inodes = dictionary.get('inodes')

class DiskInfo:
    def __init__(self, dictionary):
        self.name = dictionary.get('name')
        self.major = dictionary.get('major')
        self.minor = dictionary.get('minor')
        self.size = dictionary.get('size')
        self.scheduler = dictionary.get('scheduler')

class NetInfo:
    def __init__(self, dictionary):
        self.name = dictionary.get('name')
        self.mac_address = dictionary.get('mac_address')
        self.speed = dictionary.get('speed')
        self.mtu = dictionary.get('mtu')

class Node:
    def __init__(self, dictionary):
        self.node_id = dictionary.get('node_id')
        self.memory = dictionary.get('memory')
        self.filesystems = create_object_list(FsInfo, dictionary.get('filesystems'))
        self.caches = create_object_list(Cache, dictionary.get('caches'))
        self.cores = create_object_list(Core, dictionary.get('cores'))

class Core:
    def __init__(self, dictionary):
        self.core_id = dictionary.get('core_id')
        self.threads = dictionary.get('thread_ids')
        self.caches = create_object_list(Cache, dictionary.get('caches'))

class Cache:
    def __init__(self, dictionary):
        self.size = dictionary.get('size')
        self.cache_type = dictionary.get('type')
        self.level = dictionary.get('level')

def create_object_list(cls, dict_list):
    if dict_list:
        return [cls(dictionary) for dictionary in dict_list
                if dictionary is not None]
    return []
