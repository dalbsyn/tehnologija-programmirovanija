# нурска 4
class Fruit:
    def __init__(self, name, taste):
        self._name = name
        self._taste = taste

    def get_name(self):
        return name
    def get_taste(self):
        return taste

    def set_name(self, name):
        self.name = name
    def set_taste(self, taste):
        self.taste = taste

    def describe(self):
        print("Это фрукт")

class Apple(Fruit):
    def crunch(self):
        print("Яблоко хрустит")
    def describe(self):
        print("it is appple")
class Orange(Fruit):
    def pell(self):
        print("Апельсин очищается")
    def describe(self):
        print("it is orange")

class Banna(Fruit):
    def pell(self):
        print("Банан очищен")
    def describe(self):
        print("it is banana")

fruit = set_name("Apple")
fruit1 = set_name("Banna")
fruit2 = set_name("Orange")


