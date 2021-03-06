# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import unittest

from datetime import datetime

from cadvisor.info.v1.metric import MetricVal
from cadvisor.info.v1.container.stats import ContainerStats
from cadvisor.info.v1.container.stats import CpuCFS
from cadvisor.info.v1.container.stats import CpuStats
from cadvisor.info.v1.container.stats import CpuUsage
from cadvisor.info.v1.container.stats import DiskIoStats
from cadvisor.info.v1.container.stats import FsStats
from cadvisor.info.v1.container.stats import InterfaceStats
from cadvisor.info.v1.container.stats import LoadStats
from cadvisor.info.v1.container.stats import MemoryStats
from cadvisor.info.v1.container.stats import MemoryStatsMemoryData
from cadvisor.info.v1.container.stats import NetworkStats
from cadvisor.info.v1.container.stats import PerDiskStats
from cadvisor.info.v1.container.stats import TcpStats

class TestV1ContainerStats(unittest.TestCase):
    def test_init_container_stats_timestamp(self):
        container_stats = ContainerStats({'timestamp':'2016-08-24T21:19:24.623769018Z'})
        time = datetime(2016, 8, 24, 21, 19, 24, 623769)
        self.assertEqual(container_stats.timestamp, time)

    def test_init_container_stats_cpu(self):
        container_stats = ContainerStats({'cpu':{'load_average':123}})
        self.assertEqual(container_stats.cpu.__class__, CpuStats)
        self.assertEqual(container_stats.cpu.load_average, 123)

    def test_init_container_stats_diskio(self):
        container_stats = ContainerStats({'diskio':{'io_service_bytes':123}})
        self.assertEqual(container_stats.diskio.__class__, DiskIoStats)
        self.assertEqual(container_stats.diskio.io_service_bytes, 123)

    def test_init_container_stats_memory(self):
        container_stats = ContainerStats({'memory':{'usage':123}})
        self.assertEqual(container_stats.memory.__class__, MemoryStats)
        self.assertEqual(container_stats.memory.usage, 123)

    def test_init_container_stats_filesystem(self):
        container_stats = ContainerStats({'filesystem':[{'device':123},]})
        self.assertEqual(len(container_stats.filesystem), 1)
        self.assertEqual(container_stats.filesystem[0].__class__, FsStats)
        self.assertEqual(container_stats.filesystem[0].device, 123)

    def test_init_container_stats_task_stats(self):
        container_stats = ContainerStats({'task_stats':{'nr_sleeping':123}})
        self.assertEqual(container_stats.task_stats.__class__, LoadStats)
        self.assertEqual(container_stats.task_stats.nr_sleeping, 123)

    def test_init_container_stats_custom_metrics(self):
        metric_list = [{'metric1':123}, {'metric2':456}]
        container_stats = ContainerStats({'custom_metrics':{'test1':metric_list}})
        self.assertEqual(len(container_stats.custom_metrics['test1']), 2)
        self.assertEqual(container_stats.custom_metrics['test1'][0].__class__, MetricVal)
        self.assertEqual(container_stats.custom_metrics['test1'][1].__class__, MetricVal)

class TestV1CpuStats(unittest.TestCase):
    def test_init_cpu_stats_load_average(self):
        cpu_stats = CpuStats({'load_average':123})
        self.assertEqual(cpu_stats.load_average, 123)

    def test_init_cpu_stats_usage(self):
        cpu_stats = CpuStats({'usage':{'total':123}})
        self.assertEqual(cpu_stats.usage.__class__, CpuUsage)
        self.assertEqual(cpu_stats.usage.total, 123)

    def test_init_cpu_stats_cfs(self):
        cpu_stats = CpuStats({'cfs':{'periods':123}})
        self.assertEqual(cpu_stats.cfs.__class__, CpuCFS)
        self.assertEqual(cpu_stats.cfs.periods, 123)

class TestV1CpuUsage(unittest.TestCase):
    def test_init_cpu_usage_total(self):
        cpu_usage = CpuUsage({'total':123})
        self.assertEqual(cpu_usage.total, 123)

    def test_init_cpu_usage_per_cpu_usage(self):
        cpu_usage = CpuUsage({'per_cpu_usage':123})
        self.assertEqual(cpu_usage.per_cpu_usage, 123)

    def test_init_cpu_usage_user(self):
        cpu_usage = CpuUsage({'user':123})
        self.assertEqual(cpu_usage.user, 123)

    def test_init_cpu_usage_system(self):
        cpu_usage = CpuUsage({'system':123})
        self.assertEqual(cpu_usage.system, 123)

class TestV1CpuCFS(unittest.TestCase):
    def test_init_cpu_cFS_periods(self):
        cpu_cfs = CpuCFS({'periods':123})
        self.assertEqual(cpu_cfs.periods, 123)

    def test_init_cpu_cFS_throttled_periods(self):
        cpu_cfs = CpuCFS({'throttled_periods':123})
        self.assertEqual(cpu_cfs.throttled_periods, 123)

    def test_init_cpu_cFS_throttled_time(self):
        cpu_cfs = CpuCFS({'throttled_time':123})
        self.assertEqual(cpu_cfs.throttled_time, 123)

class TestV1LoadStats(unittest.TestCase):
    def test_init_load_stats_nr_sleeping(self):
        load_stats = LoadStats({'nr_sleeping':123})
        self.assertEqual(load_stats.nr_sleeping, 123)

    def test_init_load_stats_nr_running(self):
        load_stats = LoadStats({'nr_running':123})
        self.assertEqual(load_stats.nr_running, 123)

    def test_init_load_stats_nr_stopped(self):
        load_stats = LoadStats({'nr_stopped':123})
        self.assertEqual(load_stats.nr_stopped, 123)

    def test_init_load_stats_nr_uninterruptible(self):
        load_stats = LoadStats({'nr_uninterruptible':123})
        self.assertEqual(load_stats.nr_uninterruptible, 123)

    def test_init_load_stats_nr_io_wait(self):
        load_stats = LoadStats({'nr_io_wait':123})
        self.assertEqual(load_stats.nr_io_wait, 123)

class TestV1PerDiskStats(unittest.TestCase):
    def test_init_per_disk_stats_major(self):
        per_disk_stats = PerDiskStats({'major':123})
        self.assertEqual(per_disk_stats.major, 123)

    def test_init_per_disk_stats_minor(self):
        per_disk_stats = PerDiskStats({'minor':123})
        self.assertEqual(per_disk_stats.minor, 123)

    def test_init_per_disk_stats_stats(self):
        per_disk_stats = PerDiskStats({'stats':123})
        self.assertEqual(per_disk_stats.stats, 123)

class TestV1DiskIoStats(unittest.TestCase):
    def test_init_disk_io_stats_io_service_bytes(self):
        disk_io_stats = DiskIoStats({'io_service_bytes':123})
        self.assertEqual(disk_io_stats.io_service_bytes, 123)

    def test_init_disk_io_stats_io_serviced(self):
        disk_io_stats = DiskIoStats({'io_serviced':123})
        self.assertEqual(disk_io_stats.io_serviced, 123)

    def test_init_disk_io_stats_io_queued(self):
        disk_io_stats = DiskIoStats({'io_queued':123})
        self.assertEqual(disk_io_stats.io_queued, 123)

    def test_init_disk_io_stats_sectors(self):
        disk_io_stats = DiskIoStats({'sectors':123})
        self.assertEqual(disk_io_stats.sectors, 123)

    def test_init_disk_io_stats_io_service_time(self):
        disk_io_stats = DiskIoStats({'io_service_time':123})
        self.assertEqual(disk_io_stats.io_service_time, 123)

    def test_init_disk_io_stats_io_wait_time(self):
        disk_io_stats = DiskIoStats({'io_wait_time':123})
        self.assertEqual(disk_io_stats.io_wait_time, 123)

    def test_init_disk_io_stats_io_merged(self):
        disk_io_stats = DiskIoStats({'io_merged':123})
        self.assertEqual(disk_io_stats.io_merged, 123)

    def test_init_disk_io_stats_io_time(self):
        disk_io_stats = DiskIoStats({'io_time':123})
        self.assertEqual(disk_io_stats.io_time, 123)

class TestV1MemoryStats(unittest.TestCase):
    def test_init_memory_stats_usage(self):
        memstats = MemoryStats({'usage':123})
        self.assertEqual(memstats.usage, 123)

    def test_init_memory_stats_cache(self):
        memstats = MemoryStats({'cache':123})
        self.assertEqual(memstats.cache, 123)

    def test_init_memory_stats_rss(self):
        memstats = MemoryStats({'rss':123})
        self.assertEqual(memstats.rss, 123)

    def test_init_memory_stats_swap(self):
        memstats = MemoryStats({'swap':123})
        self.assertEqual(memstats.swap, 123)

    def test_init_memory_stats_working_set(self):
        memstats = MemoryStats({'working_set':123})
        self.assertEqual(memstats.working_set, 123)

    def test_init_memory_stats_failcnt(self):
        memstats = MemoryStats({'failcnt':123})
        self.assertEqual(memstats.failcnt, 123)

    def test_init_memory_stats_container_data_correct_type(self):
        memstats = MemoryStats({'container_data':{'test':123}})
        self.assertEqual(memstats.container_data.__class__, MemoryStatsMemoryData)

    def test_init_memory_stats_hierarchical_data_correct_type(self):
        memstats = MemoryStats({'hierarchical_data':{'test':123}})
        self.assertEqual(memstats.hierarchical_data.__class__, MemoryStatsMemoryData)

class TestV1MemoryStatsMemoryData(unittest.TestCase):
    def test_init_memory_stats_memory_data_pgfault(self):
        memstats_memdata = MemoryStatsMemoryData({'pgfault':123})
        self.assertEqual(memstats_memdata.pgfault, 123)

    def test_init_memory_stats_memory_data_pgmajfault(self):
        memstats_memdata = MemoryStatsMemoryData({'pgmajfault':123})
        self.assertEqual(memstats_memdata.pgmajfault, 123)

class TestV1InterfaceStats(unittest.TestCase):
    def test_init_interface_stats_name(self):
        iface_stats = InterfaceStats({'name':123})
        self.assertEqual(iface_stats.name, 123)

    def test_init_interface_stats_rx_bytes(self):
        iface_stats = InterfaceStats({'rx_bytes':123})
        self.assertEqual(iface_stats.rx_bytes, 123)

    def test_init_interface_stats_rx_packets(self):
        iface_stats = InterfaceStats({'rx_packets':123})
        self.assertEqual(iface_stats.rx_packets, 123)

    def test_init_interface_stats_rx_errors(self):
        iface_stats = InterfaceStats({'rx_errors':123})
        self.assertEqual(iface_stats.rx_errors, 123)

    def test_init_interface_stats_rx_dropped(self):
        iface_stats = InterfaceStats({'rx_dropped':123})
        self.assertEqual(iface_stats.rx_dropped, 123)

    def test_init_interface_stats_tx_bytes(self):
        iface_stats = InterfaceStats({'tx_bytes':123})
        self.assertEqual(iface_stats.tx_bytes, 123)

    def test_init_interface_stats_tx_packets(self):
        iface_stats = InterfaceStats({'tx_packets':123})
        self.assertEqual(iface_stats.tx_packets, 123)

    def test_init_interface_stats_tx_errors(self):
        iface_stats = InterfaceStats({'tx_errors':123})
        self.assertEqual(iface_stats.tx_errors, 123)

    def test_init_interface_stats_tx_dropped(self):
        iface_stats = InterfaceStats({'tx_dropped':123})
        self.assertEqual(iface_stats.tx_dropped, 123)

class TestV1ContainerNetworkStats(unittest.TestCase):
    def test_init_network_stats_name(self):
        net_stats = NetworkStats({'name':123})
        self.assertEqual(net_stats.name, 123)

    def test_init_network_stats_rx_bytes(self):
        net_stats = NetworkStats({'rx_bytes':123})
        self.assertEqual(net_stats.rx_bytes, 123)

    def test_init_network_stats_rx_packets(self):
        net_stats = NetworkStats({'rx_packets':123})
        self.assertEqual(net_stats.rx_packets, 123)

    def test_init_network_stats_rx_errors(self):
        net_stats = NetworkStats({'rx_errors':123})
        self.assertEqual(net_stats.rx_errors, 123)

    def test_init_network_stats_rx_dropped(self):
        net_stats = NetworkStats({'rx_dropped':123})
        self.assertEqual(net_stats.rx_dropped, 123)

    def test_init_network_stats_tx_bytes(self):
        net_stats = NetworkStats({'tx_bytes':123})
        self.assertEqual(net_stats.tx_bytes, 123)

    def test_init_network_stats_tx_packets(self):
        net_stats = NetworkStats({'tx_packets':123})
        self.assertEqual(net_stats.tx_packets, 123)

    def test_init_network_stats_tx_errors(self):
        net_stats = NetworkStats({'tx_errors':123})
        self.assertEqual(net_stats.tx_errors, 123)

    def test_init_network_stats_tx_dropped(self):
        net_stats = NetworkStats({'tx_dropped':123})
        self.assertEqual(net_stats.tx_dropped, 123)

class TestV1ContainerTcpStats(unittest.TestCase):
    def test_init_tcp_stats_established(self):
        tcp_stats = TcpStats({'Established':123})
        self.assertEqual(tcp_stats.established, 123)

    def test_init_tcp_stats_syn_sent(self):
        tcp_stats = TcpStats({'SynSent':123})
        self.assertEqual(tcp_stats.syn_sent, 123)

    def test_init_tcp_stats_syn_recv(self):
        tcp_stats = TcpStats({'SynRecv':123})
        self.assertEqual(tcp_stats.syn_recv, 123)

    def test_init_tcp_stats_fin_wait1(self):
        tcp_stats = TcpStats({'FinWait1':123})
        self.assertEqual(tcp_stats.fin_wait1, 123)

    def test_init_tcp_stats_fin_wait2(self):
        tcp_stats = TcpStats({'FinWait2':123})
        self.assertEqual(tcp_stats.fin_wait2, 123)

    def test_init_tcp_stats_time_wait(self):
        tcp_stats = TcpStats({'TimeWait':123})
        self.assertEqual(tcp_stats.time_wait, 123)

    def test_init_tcp_stats_close(self):
        tcp_stats = TcpStats({'Close':123})
        self.assertEqual(tcp_stats.close, 123)

    def test_init_tcp_stats_close_wait(self):
        tcp_stats = TcpStats({'CloseWait':123})
        self.assertEqual(tcp_stats.close_wait, 123)

    def test_init_tcp_stats_last_ack(self):
        tcp_stats = TcpStats({'LastAck':123})
        self.assertEqual(tcp_stats.last_ack, 123)

    def test_init_tcp_stats_listen(self):
        tcp_stats = TcpStats({'Listen':123})
        self.assertEqual(tcp_stats.listen, 123)

    def test_init_tcp_stats_closing(self):
        tcp_stats = TcpStats({'Closing':123})
        self.assertEqual(tcp_stats.closing, 123)

class TestV1ContainerFsStats(unittest.TestCase):
    def test_init_fs_stats_device(self):
        fs_stats = FsStats({'device':123})
        self.assertEqual(fs_stats.device, 123)

    def test_init_fs_stats_type(self):
        fs_stats = FsStats({'type':123})
        self.assertEqual(fs_stats.type, 123)

    def test_init_fs_stats_capacity(self):
        fs_stats = FsStats({'capacity':123})
        self.assertEqual(fs_stats.capacity, 123)

    def test_init_fs_stats_usage(self):
        fs_stats = FsStats({'usage':123})
        self.assertEqual(fs_stats.usage, 123)

    def test_init_fs_stats_base_usage(self):
        fs_stats = FsStats({'base_usage':123})
        self.assertEqual(fs_stats.base_usage, 123)

    def test_init_fs_stats_available(self):
        fs_stats = FsStats({'available':123})
        self.assertEqual(fs_stats.available, 123)

    def test_init_fs_stats_has_inodes(self):
        fs_stats = FsStats({'has_inodes':123})
        self.assertEqual(fs_stats.has_inodes, 123)

    def test_init_fs_stats_inodes(self):
        fs_stats = FsStats({'inodes':123})
        self.assertEqual(fs_stats.inodes, 123)

    def test_init_fs_stats_inodes_free(self):
        fs_stats = FsStats({'inodes_free':123})
        self.assertEqual(fs_stats.inodes_free, 123)

    def test_init_fs_stats_reads_completed(self):
        fs_stats = FsStats({'reads_completed':123})
        self.assertEqual(fs_stats.reads_completed, 123)

    def test_init_fs_stats_reads_merged(self):
        fs_stats = FsStats({'reads_merged':123})
        self.assertEqual(fs_stats.reads_merged, 123)

    def test_init_fs_stats_sectors_read(self):
        fs_stats = FsStats({'sectors_read':123})
        self.assertEqual(fs_stats.sectors_read, 123)

    def test_init_fs_stats_read_time(self):
        fs_stats = FsStats({'read_time':123})
        self.assertEqual(fs_stats.read_time, 123)

    def test_init_fs_stats_writes_completed(self):
        fs_stats = FsStats({'writes_completed':123})
        self.assertEqual(fs_stats.writes_completed, 123)

    def test_init_fs_stats_writes_merged(self):
        fs_stats = FsStats({'writes_merged':123})
        self.assertEqual(fs_stats.writes_merged, 123)

    def test_init_fs_stats_sectors_written(self):
        fs_stats = FsStats({'sectors_written':123})
        self.assertEqual(fs_stats.sectors_written, 123)

    def test_init_fs_stats_write_time(self):
        fs_stats = FsStats({'write_time':123})
        self.assertEqual(fs_stats.write_time, 123)

    def test_init_fs_stats_io_in_progress(self):
        fs_stats = FsStats({'io_in_progress':123})
        self.assertEqual(fs_stats.io_in_progress, 123)

    def test_init_fs_stats_io_time(self):
        fs_stats = FsStats({'io_time':123})
        self.assertEqual(fs_stats.io_time, 123)

    def test_init_fs_stats_weighted_io_time(self):
        fs_stats = FsStats({'weighted_io_time':123})
        self.assertEqual(fs_stats.weighted_io_time, 123)
