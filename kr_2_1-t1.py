# Вариант 5 - 1 задание

class Computer:
    def __init__(self):
        self.__cpu = Processor()
        self.__ram = RAM()
        self.__hd = HardDrive()
        self.__gpu = GraphicsCard()

    def get_cpu(self):
        self.__cpu.check_state()

    def get_ram(self):
        self.__ram.check_state()

    def get_hd(self):
        self.__hd.check_state()

    def get_gpu(self):
        self.__gpu.check_state()

class Processor:
    def check_state(self):
        print("Processor is online")

class RAM:
    def check_state(self):
        print("RAM is online")

class HardDrive:
    def check_state(self):
        print("Hard drive is online")

class GraphicsCard:
    def check_state(self):
        print("Graphics card is ready to be melted")

sth = Computer()

print(sth.get_cpu(), sth.get_hd(), sth.get_gpu())

