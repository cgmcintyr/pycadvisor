# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import unittest
import json

from datetime import datetime

from cadvisor.info.v1.container.stats import TcpStats
from cadvisor.info.v1.container.stats import FsStats
from cadvisor.info.v1.container.stats import NetworkStats
from cadvisor.info.v1.container.stats import InterfaceStats
from cadvisor.info.v1.container.stats import MemoryStatsMemoryData

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
        tcp_stats = TcpStats({'FinWait3':123})
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
