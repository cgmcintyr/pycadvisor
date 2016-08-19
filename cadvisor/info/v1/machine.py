# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from cadvisor.info.info import Info

class MachineInfo(Info):
    def __init__(self, dictionary):
        Info.__init__(self, dictionary)
        self.load_attr('num_cores', attr='num_cores')
        self.load_attr('cpu_frequency_khz', attr='cpu_frequency_khz')
        self.load_attr('machine_id', attr='machine_id')
        self.load_attr('system_uuid', attr='system_uuid')
        self.load_attr('boot_id', attr='boot_id')

        self.filesystems = create_object_list(FsInfo, dictionary.get('filesystems'))
        self.disk_map = create_object_list(DiskInfo, dictionary.get('disk_map'))
        self.network_devices = create_object_list(NetInfo, dictionary.get('network_devices'))
        self.topology = create_object_list(Node, dictionary.get('topology'))

        self.load_attr('cloud_provider', attr='cloud_provider')
        self.load_attr('instance_type', attr='instance_type')
        self.load_attr('instance_id', attr='instance_id')

class FsInfo(Info):
    def __init__(self, dictionary):
        Info.__init__(self, dictionary)
        self.load_attr('device', attr='device')
        self.load_attr('capacity', attr='capacity')
        self.load_attr('type', attr='fs_type')
        self.load_attr('has_inodes', attr='has_inodes')
        self.load_attr('inodes', attr='inodes')

class DiskInfo(Info):
    def __init__(self, dictionary):
        Info.__init__(self, dictionary)
        self.load_attr('name', attr='name')
        self.load_attr('major', attr='major')
        self.load_attr('minor', attr='minor')
        self.load_attr('size', attr='size')
        self.load_attr('scheduler', attr='scheduler')

class NetInfo(Info):
    def __init__(self, dictionary):
        Info.__init__(self, dictionary)
        self.load_attr('name', attr='name')
        self.load_attr('mac_address', attr='mac_address')
        self.load_attr('speed', attr='speed')
        self.load_attr('mtu', attr='mtu')

class Node(Info):
    def __init__(self, dictionary):
        Info.__init__(self, dictionary)
        self.load_attr('node_id', attr='node_id')
        self.load_attr('memory', attr='memory')
        self.filesystems = create_object_list(FsInfo, dictionary.get('filesystems'))
        self.caches = create_object_list(Cache, dictionary.get('caches'))
        self.cores = create_object_list(Core, dictionary.get('cores'))

class Core(Info):
    def __init__(self, dictionary):
        Info.__init__(self, dictionary)
        self.load_attr('core_id', attr='core_id')
        self.load_attr('thread_ids', attr='threads')
        self.caches = create_object_list(Cache, dictionary.get('caches'))

class Cache(Info):
    def __init__(self, dictionary):
        Info.__init__(self, dictionary)
        self.load_attr('size', attr='size')
        self.load_attr('type', attr='cache_type')
        self.load_attr('level', attr='level')

def create_object_list(cls, dict_list):
    if dict_list:
        return [cls(dictionary) for dictionary in dict_list
                if dictionary is not None]
    return []
