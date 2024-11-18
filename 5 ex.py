class Device:
    def __init__(self, name, battery_life):
        self._name = name
        self._battery_life = battery_life

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_battery_life(self):
        return self._battery_life

    def set_battery_life(self, battery_life):
        self._battery_life = battery_life

device = Device("Smartphone", 10)
print(device.get_name())  # Вывод: Smartphone
print(device.get_battery_life())  # Вывод: 10
