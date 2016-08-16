class FsInfo:
    def __init__(self, dictionary):
        self.device = dictionary['device']
        self.capacity = dictionary['capacity']
        self.fs_type = dictionary['type']
        self.has_inodes = dictionary['has_inodes']
        self.inodes = dictionary['inodes'] if self.has_inodes else None
