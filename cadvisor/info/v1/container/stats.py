# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from datetime import datetime

from cadvisor.info.info import Info
from cadvisor.info.v1.metric import MetricVal

class ContainerStats(Info):
    def _setup(self):
        self._load_attr('timestamp', convert=self.__to_datetime)
        self._load_attr_as('cpu', CpuStats)
        self._load_attr_as('diskio', DiskIoStats)
        self._load_attr_as('memory', MemoryStats)
        self._load_attr_as_list_of('filesystem', FsStats)
        self._load_attr_as('task_stats', LoadStats)
        self._load_attr('custom_metrics', convert=self.__to_string_metric_map)

    @staticmethod
    def __to_datetime(value):
        go_time_format = '%Y-%m-%dT%H:%M:%S.%f'
        return datetime.strptime(value[:-4], go_time_format)

    @staticmethod
    def __to_string_metric_map(value):
        metric_map = {}
        for key in value.keys():
            metric_vals = []
            for metric in value[key]:
                metric_vals.append(MetricVal(metric))
            metric_map[key] = metric_vals
        return metric_map

class CpuStats(Info):
    def _setup(self):
        self._load_attr_as('usage', CpuUsage)
        self._load_attr_as('cfs', CpuCFS)
        self._load_attr('load_average')

class CpuUsage(Info):
    def _setup(self):
        self._load_attr('total')
        self._load_attr('per_cpu_usage')
        self._load_attr('user')
        self._load_attr('system')

class CpuCFS(Info):
    def _setup(self):
        self._load_attr('periods')
        self._load_attr('throttled_periods')
        self._load_attr('throttled_time')

class LoadStats(Info):
    def _setup(self):
        self._load_attr('nr_sleeping')
        self._load_attr('nr_running')
        self._load_attr('nr_stopped')
        self._load_attr('nr_uninterruptible')
        self._load_attr('nr_io_wait')

class PerDiskStats(Info):
    def _setup(self):
        self._load_attr('major')
        self._load_attr('minor')
        self._load_attr('stats')

class DiskIoStats(Info):
    def _setup(self):
        self._load_attr('io_service_bytes')
        self._load_attr('io_serviced')
        self._load_attr('io_queued')
        self._load_attr('sectors')
        self._load_attr('io_service_time')
        self._load_attr('io_wait_time')
        self._load_attr('io_merged')
        self._load_attr('io_time')

class MemoryStats(Info):
    def _setup(self):
        self._load_attr('usage')
        self._load_attr('cache')
        self._load_attr('rss')
        self._load_attr('swap')
        self._load_attr('working_set')
        self._load_attr('failcnt')
        self._load_attr_as('container_data', MemoryStatsMemoryData)
        self._load_attr_as('hierarchical_data', MemoryStatsMemoryData)

class MemoryStatsMemoryData(Info):
    def _setup(self):
        self._load_attr('pgfault')
        self._load_attr('pgmajfault')

class InterfaceStats(Info):
    def __init__(self, dictionary, parent=None, **kwargs):
        if self.__validate_parent(parent): self.parent = parent
        Info.__init__(self, dictionary, **kwargs)

    def _setup(self):
        self._load_attr('name')
        self._load_attr('rx_bytes')
        self._load_attr('rx_packets')
        self._load_attr('rx_errors')
        self._load_attr('rx_dropped')
        self._load_attr('tx_bytes')
        self._load_attr('tx_packets')
        self._load_attr('tx_errors')
        self._load_attr('tx_dropped')

        if self.parent:
            for k, v in vars(self).items():
                if not k.startswith('_'):
                    setattr(self.parent, k, v)

    def __validate_parent(self, parent):
        if parent is None:
            pass
        elif parent.__class__ is not NetworkStats:
            msg = 'parent must have type None or be an instance of NetworkStats'
            raise TypeError(msg)
        return True

class NetworkStats(Info):
    def _setup(self):
        InterfaceStats(self._data, parent=self)
        self._load_attr_as_list_of('interfaces', InterfaceStats)
        self._load_attr_as('tcp', TcpStats)
        self._load_attr_as('tcp6', TcpStats)

class TcpStats(Info):
    def _setup(self):
        self._load_attr('Established', attr='established')
        self._load_attr('SynSent', attr='syn_sent')
        self._load_attr('SynRecv', attr='syn_recv')
        self._load_attr('FinWait1', attr='fin_wait1')
        self._load_attr('FinWait2', attr='fin_wait2')
        self._load_attr('TimeWait', attr='time_wait')
        self._load_attr('Close', attr='close')
        self._load_attr('CloseWait', attr='close_wait')
        self._load_attr('LastAck', attr='last_ack')
        self._load_attr('Listen', attr='listen')
        self._load_attr('Closing', attr='closing')

class FsStats(Info):
    def _setup(self):
        self._load_attr('device')
        self._load_attr('type')
        self._load_attr('capacity')
        self._load_attr('usage')
        self._load_attr('base_usage')
        self._load_attr('available')
        self._load_attr('has_inodes')
        self._load_attr('inodes')
        self._load_attr('inodes_free')
        self._load_attr('reads_completed')
        self._load_attr('reads_merged')
        self._load_attr('sectors_read')
        self._load_attr('read_time')
        self._load_attr('writes_completed')
        self._load_attr('writes_merged')
        self._load_attr('sectors_written')
        self._load_attr('write_time')
        self._load_attr('io_in_progress')
        self._load_attr('io_time')
        self._load_attr('weighted_io_time')
