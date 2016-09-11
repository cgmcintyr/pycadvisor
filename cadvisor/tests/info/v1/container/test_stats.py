# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import unittest
import json

from datetime import datetime

from cadvisor.info.v1.container.stats import TcpStats
from cadvisor.info.v1.container.stats import FsStats
from cadvisor.info.v1.container.stats import NetworkStats

class TestV1ContainerNetworkStats(unittest.TestCase):
    def test_init_network_stats_name(self):
        netstats = NetworkStats({'name':123})
        self.assertEqual(netstats.name, 123)

    def test_init_network_stats_rx_bytes(self):
        netstats = NetworkStats({'rx_bytes':123})
        self.assertEqual(netstats.rx_bytes, 123)

    def test_init_network_stats_rx_packets(self):
        netstats = NetworkStats({'rx_packets':123})
        self.assertEqual(netstats.rx_packets, 123)

    def test_init_network_stats_rx_errors(self):
        netstats = NetworkStats({'rx_errors':123})
        self.assertEqual(netstats.rx_errors, 123)

    def test_init_network_stats_rx_dropped(self):
        netstats = NetworkStats({'rx_dropped':123})
        self.assertEqual(netstats.rx_dropped, 123)

    def test_init_network_stats_tx_bytes(self):
        netstats = NetworkStats({'tx_bytes':123})
        self.assertEqual(netstats.tx_bytes, 123)

    def test_init_network_stats_tx_packets(self):
        netstats = NetworkStats({'tx_packets':123})
        self.assertEqual(netstats.tx_packets, 123)

    def test_init_network_stats_tx_errors(self):
        netstats = NetworkStats({'tx_errors':123})
        self.assertEqual(netstats.tx_errors, 123)

    def test_init_network_stats_tx_dropped(self):
        netstats = NetworkStats({'tx_dropped':123})
        self.assertEqual(netstats.tx_dropped, 123)

class TestV1ContainerTcpStats(unittest.TestCase):
    def test_init_tcp_stats_established(self):
        tcpstats = TcpStats({'established':123})
        self.assertEqual(tcpstats.established, 123)

    def test_init_tcp_stats_syn_sent(self):
        tcpstats = TcpStats({'syn_sent':123})
        self.assertEqual(tcpstats.syn_sent, 123)

    def test_init_tcp_stats_syn_recv(self):
        tcpstats = TcpStats({'syn_recv':123})
        self.assertEqual(tcpstats.syn_recv, 123)

    def test_init_tcp_stats_fin_wait1(self):
        tcpstats = TcpStats({'fin_wait1':123})
        self.assertEqual(tcpstats.fin_wait1, 123)

    def test_init_tcp_stats_fin_wait2(self):
        tcpstats = TcpStats({'fin_wait2':123})
        self.assertEqual(tcpstats.fin_wait2, 123)

    def test_init_tcp_stats_time_wait(self):
        tcpstats = TcpStats({'time_wait':123})
        self.assertEqual(tcpstats.time_wait, 123)

    def test_init_tcp_stats_close(self):
        tcpstats = TcpStats({'close':123})
        self.assertEqual(tcpstats.close, 123)

    def test_init_tcp_stats_close_wait(self):
        tcpstats = TcpStats({'close_wait':123})
        self.assertEqual(tcpstats.close_wait, 123)

    def test_init_tcp_stats_last_ack(self):
        tcpstats = TcpStats({'last_ack':123})
        self.assertEqual(tcpstats.last_ack, 123)

    def test_init_tcp_stats_listen(self):
        tcpstats = TcpStats({'listen':123})
        self.assertEqual(tcpstats.listen, 123)

    def test_init_tcp_stats_closing(self):
        tcpstats = TcpStats({'closing':123})
        self.assertEqual(tcpstats.Closing, 123)

class TestV1ContainerFsStats(unittest.TestCase):
    def test_init_fs_stats_device(self):
        fsstats = FsStats({'device':123})
        self.assertEqual(fsstats.device, 123)

    def test_init_fs_stats_type(self):
        fsstats = FsStats({'type':123})
        self.assertEqual(fsstats.type, 123)

    def test_init_fs_stats_capacity(self):
        fsstats = FsStats({'capacity':123})
        self.assertEqual(fsstats.capacity, 123)

    def test_init_fs_stats_usage(self):
        fsstats = FsStats({'usage':123})
        self.assertEqual(fsstats.usage, 123)

    def test_init_fs_stats_base_usage(self):
        fsstats = FsStats({'base_usage':123})
        self.assertEqual(fsstats.base_usage, 123)

    def test_init_fs_stats_available(self):
        fsstats = FsStats({'available':123})
        self.assertEqual(fsstats.available, 123)

    def test_init_fs_stats_has_inodes(self):
        fsstats = FsStats({'has_inodes':123})
        self.assertEqual(fsstats.has_inodes, 123)

    def test_init_fs_stats_inodes(self):
        fsstats = FsStats({'inodes':123})
        self.assertEqual(fsstats.inodes, 123)

    def test_init_fs_stats_inodes_free(self):
        fsstats = FsStats({'inodes_free':123})
        self.assertEqual(fsstats.inodes_free, 123)

    def test_init_fs_stats_reads_completed(self):
        fsstats = FsStats({'reads_completed':123})
        self.assertEqual(fsstats.reads_completed, 123)

    def test_init_fs_stats_reads_merged(self):
        fsstats = FsStats({'reads_merged':123})
        self.assertEqual(fsstats.reads_merged, 123)

    def test_init_fs_stats_sectors_read(self):
        fsstats = FsStats({'sectors_read':123})
        self.assertEqual(fsstats.sectors_read, 123)

    def test_init_fs_stats_read_time(self):
        fsstats = FsStats({'read_time':123})
        self.assertEqual(fsstats.read_time, 123)

    def test_init_fs_stats_writes_completed(self):
        fsstats = FsStats({'writes_completed':123})
        self.assertEqual(fsstats.writes_completed, 123)

    def test_init_fs_stats_writes_merged(self):
        fsstats = FsStats({'writes_merged':123})
        self.assertEqual(fsstats.writes_merged, 123)

    def test_init_fs_stats_sectors_written(self):
        fsstats = FsStats({'sectors_written':123})
        self.assertEqual(fsstats.sectors_written, 123)

    def test_init_fs_stats_write_time(self):
        fsstats = FsStats({'write_time':123})
        self.assertEqual(fsstats.write_time, 123)

    def test_init_fs_stats_io_in_progress(self):
        fsstats = FsStats({'io_in_progress':123})
        self.assertEqual(fsstats.io_in_progress, 123)

    def test_init_fs_stats_io_time(self):
        fsstats = FsStats({'io_time':123})
        self.assertEqual(fsstats.io_time, 123)

    def test_init_fs_stats_weighted_io_time(self):
        fsstats = FsStats({'weighted_io_time':123})
        self.assertEqual(fsstats.weighted_io_time, 123)
