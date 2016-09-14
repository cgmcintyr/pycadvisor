# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from datetime import datetime

from cadvisor.info.info import Info
from cadvisor.info.v1.metric import MetricVal

class ContainerStats(Info):
    def setup(self):
        self.load_attr('timestamp', convert=self.__to_datetime)
        self.load_attr_info('cpu', CpuStats)
        self.load_attr_info('diskio', DiskIoStats)
        self.load_attr_info('memory', MemoryStats)
        self.load_attr_info_list('filesystem', FsStats)
        self.load_attr_info('task_stats', LoadStats)
        self.load_attr('custom_metrics', convert=self.__to_string_metric_map)

    @staticmethod
    def __to_datetime(value):
        go_time_format = '%Y-%m-%dT%H:%M:%S.%f'
        return datetime.strptime(value[:-4], go_time_format)

    @staticmethod
    def __to_string_metric_map(value):
        for key in value.keys():
            metric_vals = []
            for metric in value[key]:
                metric_vals.append(MetricVal(metric))
            value[key] = metric_vals

class CpuStats(Info):
    def setup(self):
        self.load_attr_info('usage', CpuUsage)
        self.load_attr_info('cfs', CpuCFS)
        self.load_attr('load_average')

class CpuUsage(Info):
    def setup(self):
        self.load_attr('total')
        self.load_attr('per_cpu_usage')
        self.load_attr('user')
        self.load_attr('system')

class CpuCFS(Info):
    def setup(self):
        self.load_attr('periods')
        self.load_attr('throttled_periods')
        self.load_attr('throttled_time')

class LoadStats(Info):
    def setup(self):
        self.load_attr('nr_sleeping')
        self.load_attr('nr_running')
        self.load_attr('nr_stopped')
        self.load_attr('nr_uninterruptible')
        self.load_attr('nr_io_wait')

class PerDiskStats(Info):
    def setup(self):
        self.load_attr('major')
        self.load_attr('minor')
        self.load_attr('stats')

class DiskIoStats(Info):
    def setup(self):
        self.load_attr('io_service_bytes')
        self.load_attr('io_serviced')
        self.load_attr('io_queued')
        self.load_attr('sectors')
        self.load_attr('io_service_time')
        self.load_attr('io_wait_time')
        self.load_attr('io_merged')
        self.load_attr('io_time')

class MemoryStats(Info):
    def setup(self):
        self.load_attr('usage')
        self.load_attr('cache')
        self.load_attr('rss')
        self.load_attr('swap')
        self.load_attr('working_set')
        self.load_attr('failcnt')
        self.load_attr_info('container_data', MemoryStatsMemoryData)
        self.load_attr_info('hierarchical_data', MemoryStatsMemoryData)

class MemoryStatsMemoryData(Info):
    def setup(self):
        self.load_attr('pgfault')
        self.load_attr('pgmajfault')

class InterfaceStats(Info):
    def __init__(self, dictionary, parent=None, **kwargs):
        if self.__validate_parent(parent): self.parent = parent
        Info.__init__(self, dictionary, **kwargs)

    def setup(self):
        self.load_attr('name')
        self.load_attr('rx_bytes')
        self.load_attr('rx_packets')
        self.load_attr('rx_errors')
        self.load_attr('rx_dropped')
        self.load_attr('tx_bytes')
        self.load_attr('tx_packets')
        self.load_attr('tx_errors')
        self.load_attr('tx_dropped')

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
    def setup(self):
        InterfaceStats(self._data, parent=self)
        self.load_attr_info_list('interfaces', InterfaceStats)
        self.load_attr_info('tcp', TcpStats)
        self.load_attr_info('tcp6', TcpStats)

class TcpStats(Info):
    def setup(self):
        self.load_attr('Established', attr='established')
        self.load_attr('SynSent', attr='syn_sent')
        self.load_attr('SynRecv', attr='syn_recv')
        self.load_attr('FinWait1', attr='fin_wait1')
        self.load_attr('FinWait2', attr='fin_wait2')
        self.load_attr('TimeWait', attr='time_wait')
        self.load_attr('Close', attr='close')
        self.load_attr('CloseWait', attr='close_wait')
        self.load_attr('LastAck', attr='last_ack')
        self.load_attr('Listen', attr='listen')
        self.load_attr('Closing', attr='closing')

class FsStats(Info):
    def setup(self):
        self.load_attr('device')
        self.load_attr('type')
        self.load_attr('capacity')
        self.load_attr('usage')
        self.load_attr('base_usage')
        self.load_attr('available')
        self.load_attr('has_inodes')
        self.load_attr('inodes')
        self.load_attr('inodes_free')
        self.load_attr('reads_completed')
        self.load_attr('reads_merged')
        self.load_attr('sectors_read')
        self.load_attr('read_time')
        self.load_attr('writes_completed')
        self.load_attr('writes_merged')
        self.load_attr('sectors_written')
        self.load_attr('write_time')
        self.load_attr('io_in_progress')
        self.load_attr('io_time')
        self.load_attr('weighted_io_time')
