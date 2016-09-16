# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import unittest

from datetime import datetime

from cadvisor.info.v1.container.event import Event
from cadvisor.info.v1.container.event import EventData
from cadvisor.info.v1.container.event import OomKillEventData

class TestV1ContainerEvent(unittest.TestCase):
    def test_init_container_event_container_name(self):
        event = Event({'container_name':123})
        self.assertEqual(event.container_name, 123)

    def test_init_container_event_timestamp(self):
        data = {'timestamp':'2016-08-24T21:19:24.623769018Z'}
        time = datetime(2016, 8, 24, 21, 19, 24, 623769)
        self.assertEqual(Event(data).timestamp, time)

    def test_init_container_event_type(self):
        event = Event({'event_type':123})
        self.assertEqual(event.event_type, 123)

    def test_init_container_event_type(self):
        event = Event({'event_data':{'test':123}})
        self.assertEqual(event.event_data.__class__, EventData)

class TestV1ContainerEventData(unittest.TestCase):
    def test_init_event_data_oom(self):
        event_data = EventData({'oom':{'test':123}})
        self.assertEqual(event_data.oom.__class__, OomKillEventData)

    def test_init_event_data_omit_oom(self):
        event_data = EventData({})
        self.assertEqual(event_data.oom, None)

class TestV1ContainerOomKillEventData(unittest.TestCase):
    def test_init_oom_kill_event_data_pid(self):
        oom_kill_event_data = OomKillEventData({'pid':123})
        self.assertEqual(oom_kill_event_data.pid, 123)

    def test_init_oom_kill_event_data_process_name(self):
        oom_kill_event_data = OomKillEventData({'process_name':123})
        self.assertEqual(oom_kill_event_data.process_name, 123)
