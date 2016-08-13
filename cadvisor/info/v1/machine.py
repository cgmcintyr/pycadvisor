from collections import namedtuple
import inspect

class MachineInfo:
    def convert(name, dictionary):
        for key, value in dictionary.iteritems():
            if isinstance(value, dict):
                dictionary[key] = convert(value)
        return namedtuple(

