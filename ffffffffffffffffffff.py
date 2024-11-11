class Device:
    def init(self, name, battery_life):
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

# 2. Наследование
class Smartphone(Device):
    def call(self):
        print("Телефон звонит")
    
    def use(self):
        print("Смартфон используется для звонков и приложений")

class Laptop(Device):
    def compile_code(self):
        print("Ноутбук компилирует код")
    
    def use(self):
        print("Ноутбук используется для программирования и работы")

class Tablet(Device):
    def draw(self):
        print("Планшет используется для рисования")
    
    def use(self):
        print("Планшет используется для мультимедиа и рисования")

# 3. Полиморфизм (Overriding)
# Создаем объекты классов
smartphone = Smartphone("iPhone", 80)
laptop = Laptop("MacBook", 90)
tablet = Tablet("iPad", 70)

# Список с объектами
devices = [smartphone, laptop, tablet]

# Вызов метода use() для каждого объекта
for device in devices:
    device.use()