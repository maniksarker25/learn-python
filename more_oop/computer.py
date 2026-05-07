# composition (Has a relation)

class CPU:
    def __init__(self,core):
        self.core = core


class Ram:
    def __init__(self,size):
        self.size = size
    
class HardDrive:
    def __init__(self,capacity):
        self.capacity = capacity

# composition
class Computer:
    def __init__(self,core,ram_size,hard_capacity):
        self.cpu = CPU(core)
        self.ram = Ram(ram_size)
        self.hard_disk = HardDrive(hard_capacity)


mac = Computer(8,16,2300)