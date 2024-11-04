#5 вариант
#1
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

#2 #3
class Smartphone(Device):
    def call(self):
        print("Телефон звонит")

    def use(self):
        self.call()

class Laptop(Device):
    def compile_code(self):
        print("Ноутбук компилирует код")
 
    def use(self):
        self.compile_code()

class Tablet(Device):
    def draw(self):
        print("Планшет используется для рисования")

    def use(self):
        self.draw()

device = Device("asd", "qweqweqwe")
