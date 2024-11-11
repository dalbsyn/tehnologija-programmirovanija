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
    class Smartphone(Device):
        super.__init__(name, battery_life)
        def call(self):
            print("Телефон звонит")
        def use(self):
            print("Телефон используется")

    class Laptop:
        def compile_code(self):
            print("Ноутбук компилирует код")
        def use(self):
            print("Ноутбук используется")

    class Tablet:
        def draw(self):
            print("Планшет используется для рисования")
        def use(self):
            print("Планшет используется")

aplephon = Device.Smartphone()
sasungtablo = Device.Tablet()
huweilap = Device.Laptop()

aplephon.set_name, aplephon.set_battery_life = "aplephon", "85"

print(aplephon.get_name())
