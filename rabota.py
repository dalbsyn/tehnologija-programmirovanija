class Device:
    def __init__(self, name, battery_life):
        self._name = name
        self._battery_life = battery_life

    # Геттеры
    def get_name(self):
        return self._name

    def get_battery_life(self):
        return self._battery_life

    # Сеттеры
    def set_name(self, value):
        self._name = value

    def set_battery_life(self, value):
        self._battery_life = value

    # Второе задание
    class Smartphone:
        def call(self):
            print("Телефон звонит")

    class Laptop:
        def compile_code(self):
            print("Ноутбук компилирует код")

    class Tablet:
        def draw(self):
            print("Планшет используется для рисования")

tabs4 = Device.Tablet()

tabs4.draw()

