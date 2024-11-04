class Device:
    def __init__(self, name, battery_life):
        self.__name = name
        self.__battery_life = battery_life

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_battery_life(self):
        return self.__battery_life

    def set_battery_life(self, battery_life):
        self.__battery_life = battery_life

device = Device("laptop", 6)

print(device.get_name())          
print(device.get_battery_life())   


device.set_name("Phone")
device.set_battery_life(10)


print(device.get_name())          
print(device.get_battery_life())   
