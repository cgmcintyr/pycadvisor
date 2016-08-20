# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from cadvisor.info.info import Info


class MachineInfo(Info):
    def __init__(self, dictionary, **kwargs):
        Info.__init__(self, dictionary, **kwargs)

    def setup(self):
        self.load_attr('num_cores', attr='num_cores')
        self.load_attr('cpu_frequency_khz', attr='cpu_frequency_khz')
        self.load_attr('machine_id', attr='machine_id')
        self.load_attr('system_uuid', attr='system_uuid')
        self.load_attr('boot_id', attr='boot_id')

        self.load_attr_object_list('filesystems', FsInfo)
        self.load_attr_object_list('disk_map', DiskInfo)
        self.load_attr_object_list('network_devices', NetInfo)
        self.load_attr_object_list('topology', Node)

        self.load_attr('cloud_provider', attr='cloud_provider')
        self.load_attr('instance_type', attr='instance_type')
        self.load_attr('instance_id', attr='instance_id')

class FsInfo(Info):
    def __init__(self, dictionary, **kwargs):
        Info.__init__(self, dictionary, **kwargs)

    def setup(self):
        self.load_attr('device', attr='device')
        self.load_attr('capacity', attr='capacity')
        self.load_attr('type', attr='fs_type')
        self.load_attr('has_inodes', attr='has_inodes')
        self.load_attr('inodes', attr='inodes')

class DiskInfo(Info):
    def __init__(self, dictionary, **kwargs):
        Info.__init__(self, dictionary, **kwargs)

    def setup(self):
        self.load_attr('name', attr='name')
        self.load_attr('major', attr='major')
        self.load_attr('minor', attr='minor')
        self.load_attr('size', attr='size')
        self.load_attr('scheduler', attr='scheduler')

class NetInfo(Info):
    def __init__(self, dictionary, **kwargs):
        Info.__init__(self, dictionary, **kwargs)

    def setup(self):
        self.load_attr('name', attr='name')
        self.load_attr('mac_address', attr='mac_address')
        self.load_attr('speed', attr='speed')
        self.load_attr('mtu', attr='mtu')

class Node(Info):
    def __init__(self, dictionary, **kwargs):
        Info.__init__(self, dictionary, **kwargs)

    def setup(self):
        self.load_attr('node_id', attr='node_id')
        self.load_attr('memory', attr='memory')
        self.load_attr_object_list('filesystems', FsInfo)
        self.load_attr_object_list('caches', Cache)
        self.load_attr_object_list('cores', Core)


class Core(Info):
    def __init__(self, dictionary, **kwargs):
        Info.__init__(self, dictionary, **kwargs)

    def setup(self):
        self.load_attr('core_id', attr='core_id')
        self.load_attr('thread_ids', attr='threads')
        self.load_attr_object_list('caches', Cache)

class Cache(Info):
    def __init__(self, dictionary, **kwargs):
        Info.__init__(self, dictionary, **kwargs)

    def setup(self):
        self.load_attr('size', attr='size')
        self.load_attr('type', attr='cache_type')
        self.load_attr('level', attr='level')
