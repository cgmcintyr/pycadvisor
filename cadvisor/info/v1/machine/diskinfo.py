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

class DiskInfo:
    def __init__(self, dictionary):
        self.name = dictionary['name']
        self.major = dictionary['major']
        self.minor = dictrionary['minor']
        size

                                                    // I/O Scheduler - one of "none", "noop", "cfq", "deadline"
                                                        Scheduler string `json:"scheduler"`
                                                        }

        type NetInfo struct {
                    // Device name
                        Name string `json:"name"`

                            // Mac Address
                                MacAddress string `json:"mac_address"`

                                    // Speed in MBits/s
                                        Speed int64 `json:"speed"`

                                            // Maximum Transmission Unit
                                                Mtu int64 `json:"mtu"`
                                                }

                }
                }
