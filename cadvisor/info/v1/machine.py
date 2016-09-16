# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from cadvisor.info.info import Info

class MachineInfo(Info):
    def __init__(self, dictionary, **kwargs):
        Info.__init__(self, dictionary, **kwargs)

    def _setup(self):
        self._load_attr('num_cores')
        self._load_attr('cpu_frequency_khz')
        self._load_attr('machine_id')
        self._load_attr('system_uuid')
        self._load_attr('boot_id')

        self._load_attr_as_list_of('filesystems', FsInfo)
        self._load_attr('disk_map', convert=self.__to_string_disk_map)
        self._load_attr_as_list_of('network_devices', NetInfo)
        self._load_attr_as_list_of('topology', Node)

        self._load_attr('cloud_provider')
        self._load_attr('instance_type')
        self._load_attr('instance_id')

    @staticmethod
    def __to_string_disk_map(value):
        disk_map = {}
        for key in value.keys():
            disk_map[key] = DiskInfo(value[key])
        return disk_map

class FsInfo(Info):
    def __init__(self, dictionary, **kwargs):
        Info.__init__(self, dictionary, **kwargs)

    def _setup(self):
        self._load_attr('device')
        self._load_attr('capacity')
        self._load_attr('type', attr='fs_type')
        self._load_attr('has_inodes')
        self._load_attr('inodes')

class DiskInfo(Info):
    def __init__(self, dictionary, **kwargs):
        Info.__init__(self, dictionary, **kwargs)

    def _setup(self):
        self._load_attr('name')
        self._load_attr('major')
        self._load_attr('minor')
        self._load_attr('size')
        self._load_attr('scheduler')

class NetInfo(Info):
    def __init__(self, dictionary, **kwargs):
        Info.__init__(self, dictionary, **kwargs)

    def _setup(self):
        self._load_attr('name')
        self._load_attr('mac_address')
        self._load_attr('speed')
        self._load_attr('mtu')

class Node(Info):
    def __init__(self, dictionary, **kwargs):
        Info.__init__(self, dictionary, **kwargs)

    def _setup(self):
        self._load_attr('node_id')
        self._load_attr('memory')
        self._load_attr_as_list_of('filesystems', FsInfo)
        self._load_attr_as_list_of('caches', Cache)
        self._load_attr_as_list_of('cores', Core)


class Core(Info):
    def __init__(self, dictionary, **kwargs):
        Info.__init__(self, dictionary, **kwargs)

    def _setup(self):
        self._load_attr('core_id')
        self._load_attr('thread_ids', attr='threads')
        self._load_attr_as_list_of('caches', Cache)

class Cache(Info):
    def __init__(self, dictionary, **kwargs):
        Info.__init__(self, dictionary, **kwargs)

    def _setup(self):
        self._load_attr('size')
        self._load_attr('type', attr='cache_type')
        self._load_attr('level')
