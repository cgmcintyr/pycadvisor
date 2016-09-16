# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from datetime import datetime

from cadvisor.info.info import Info

class Event(Info):
    def setup(self):
        self.load_attr('container_name')
        self.load_attr('timestamp', convert=self.__to_datetime)
        self.load_attr('event_type')
        self.load_attr_info('event_data', EventData)

    @staticmethod
    def __to_datetime(value):
        go_time_format = '%Y-%m-%dT%H:%M:%S.%f'
        return datetime.strptime(value[:-4], go_time_format)

class EventData(Info):
    def setup(self):
        self.load_attr_info('oom', OomKillEventData)

class OomKillEventData(Info):
    def setup(self):
        self.load_attr('pid')
        self.load_attr('process_name')
