class Node:
    def __init__(self, dictionary):
        self.node_id = dictionary['node_id']
        self.memory = dictionary['memory']
        self.caches = [Cache(cache) for cache in dictionary['caches']]

class Core:
    def __init__(self, dictionary):
        self.core_id = json['core_id']
        self.threads = json['thread_ids']
        self.caches = [Cache(cache) for cache in dictionary['caches']]

class Cache:
    def __init__(self, dictionary):
        self.size = json['size']
        self.cache_type = dictionary['type']
        self.level = dictionary['level']
