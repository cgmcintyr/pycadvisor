from collections import namedtuple
import inspect

class MachineInfo:
    def __init__(self, url):
        self._fs_info = []
		self._node_info = []
		self._FsInfo = namedtuple('FsInfo', ['device', 'capacity', 'type', 'inodes', 'has_inodes']) 
		self._Node = namedtuple('Node', ['id', 'memory', 'cores', 'caches'])
		self._Core = namedtuple('Core', ['id', 'threads', 'caches'])
		self._Cache = namedtuple('Cache' ['size', 'type', 'level'])

	def add_fs_info(device, capacity, type, inodes, has_inodes):
		fs_info = self._FsInfo(device, capacity, type, inodes, has_inodes)
		self._fs_info.add(fs_info)
		return _FsInfo
		
	def get_fs_info():
		return _fs_info

	def add_node_info(id. memory, cores, cache):
		node = self._Node(id, memory, cores, cache)
		
	def get_node_info()
		return self._node_info
	
	def add_thread(node, thread, core_id):
		# Assume one hyperthread per core when topology data is missing
		if core_id == -1: core_id = thread
		if core_id in node.cores:
			core = Core()
			
		