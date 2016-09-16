# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from datetime import datetime

from cadvisor.info.info import Info

class Event(Info):
    def _setup(self):
        self._load_attr('container_name')
        self._load_attr('timestamp', convert=self.__to_datetime)
        self._load_attr('event_type')
        self._load_attr_as('event_data', EventData)

    @staticmethod
    def __to_datetime(value):
        go_time_format = '%Y-%m-%dT%H:%M:%S.%f'
        return datetime.strptime(value[:-4], go_time_format)

class EventData(Info):
    def _setup(self):
        self._load_attr_as('oom', OomKillEventData)

class OomKillEventData(Info):
    def _setup(self):
        self._load_attr('pid')
        self._load_attr('process_name')
