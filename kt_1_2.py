# 2 вариант
class ZooAnimal():
    def __init__(self, species, weight):
        self._species = species
        self._weight = weight
    
    def sound(self):
        print("Животное издает звук")

    def get_weight(self):
        print(self._weight)

    def get_species(self):
        print(self._species)

    def set_species(self, value):
        self._species = value

    def set_weight(self, value):
        self._weight = value

class Lion(ZooAnimal):
    def roar(self):
        print("Лев рычит")
    def sound(self):
        print("ЛЕВ РЫЧИТ")

class Elephant(ZooAnimal):
    def trumpet(self):
        print("Слон трубит")
    def sound(self):
        print("СЛОН ТРУБИТ ОЧЕНЬ СИЛЬНО")

class Penguin(ZooAnimal):
    def swim(self):
        print("Пингвин плавает")
    def sound(self):
        print("ПИНГВИН ПЛАВАЕТ КАК ТОРПЕДА")

# Животное
generic_animal = ZooAnimal(None, None)
generic_animal.sound()

# Лев
lion = Lion(None, None)

lion.set_weight("123")
lion.set_species("Nikita")

lion.get_weight()
lion.get_species()
lion.roar()
lion.sound()

