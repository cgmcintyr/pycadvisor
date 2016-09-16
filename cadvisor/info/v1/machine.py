# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from cadvisor.info.info import Info

class MachineInfo(Info):
    def __init__(self, dictionary, **kwargs):
        Info.__init__(self, dictionary, **kwargs)

    def setup(self):
        self.load_attr('num_cores')
        self.load_attr('cpu_frequency_khz')
        self.load_attr('machine_id')
        self.load_attr('system_uuid')
        self.load_attr('boot_id')

        self.load_attr_info_list('filesystems', FsInfo)
        self.load_attr('disk_map', convert=self.__to_string_disk_map)
        self.load_attr_info_list('network_devices', NetInfo)
        self.load_attr_info_list('topology', Node)

        self.load_attr('cloud_provider')
        self.load_attr('instance_type')
        self.load_attr('instance_id')

    @staticmethod
    def __to_string_disk_map(value):
        disk_map = {}
        for key in value.keys():
            disk_map[key] = DiskInfo(value[key])
        return disk_map

class FsInfo(Info):
    def __init__(self, dictionary, **kwargs):
        Info.__init__(self, dictionary, **kwargs)

    def setup(self):
        self.load_attr('device')
        self.load_attr('capacity')
        self.load_attr('type', attr='fs_type')
        self.load_attr('has_inodes')
        self.load_attr('inodes')

class DiskInfo(Info):
    def __init__(self, dictionary, **kwargs):
        Info.__init__(self, dictionary, **kwargs)

    def setup(self):
        self.load_attr('name')
        self.load_attr('major')
        self.load_attr('minor')
        self.load_attr('size')
        self.load_attr('scheduler')

class NetInfo(Info):
    def __init__(self, dictionary, **kwargs):
        Info.__init__(self, dictionary, **kwargs)

    def setup(self):
        self.load_attr('name')
        self.load_attr('mac_address')
        self.load_attr('speed')
        self.load_attr('mtu')

class Node(Info):
    def __init__(self, dictionary, **kwargs):
        Info.__init__(self, dictionary, **kwargs)

    def setup(self):
        self.load_attr('node_id')
        self.load_attr('memory')
        self.load_attr_info_list('filesystems', FsInfo)
        self.load_attr_info_list('caches', Cache)
        self.load_attr_info_list('cores', Core)


class Core(Info):
    def __init__(self, dictionary, **kwargs):
        Info.__init__(self, dictionary, **kwargs)

    def setup(self):
        self.load_attr('core_id')
        self.load_attr('thread_ids', attr='threads')
        self.load_attr_info_list('caches', Cache)

class Cache(Info):
    def __init__(self, dictionary, **kwargs):
        Info.__init__(self, dictionary, **kwargs)

    def setup(self):
        self.load_attr('size')
        self.load_attr('type', attr='cache_type')
        self.load_attr('level')
