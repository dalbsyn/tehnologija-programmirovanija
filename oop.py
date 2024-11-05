class Device:
    def __init__(self, name, battery_life):
        self._name = name          # приватное поле для имени устройства
        self._battery_life = battery_life  # приватное поле для времени работы от батареи

    # Метод для получения значения имени устройства
    def get_name(self):
        return self._name

    # Метод для изменения имени устройства
    def set_name(self, name):
        self._name = name

    # Метод для получения времени работы от батареи
    def get_battery_life(self):
        return self._battery_life

    # Метод для изменения времени работы от батареи
    def set_battery_life(self, battery_life):
        self._battery_life = battery_life
device = Device("Phone", 12)
print(device.get_name())  # Вывод: Phone
print(device.get_battery_life())  # Вывод: 12

# Изменение значений
device.set_name("Laptop")
device.set_battery_life(8)

print(device.get_name())  # Вывод: Laptop
print(device.get_battery_life())  # Вывод: 8
