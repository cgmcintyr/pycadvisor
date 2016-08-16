class V1MachineInfo:
    def __init__(self, json):
        self.num_cores = json['num_cores']
        self.cpu_frequency_khz = json['cpu_frequency_khz']
        self.memory_capacity = json['memory_capacity']
        self.machine_id = json['machine_id']
        self.system_uuid = json['system_uuid']
        self.boot_id = json['boot_id']
        self.cloud_provider = json['cloud_provider']
        self.instance_type = json['instance_type']
        self.instance_id = json['instance_id']
