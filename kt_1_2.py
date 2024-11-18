# 2 вариант
class ZooAnimal():
    def __init__(self, species, weight):
        self._species = species
        self._weight = weight
    
    def sound(self):
        print("Животное издает звук")

    def set_species(self, value):
        self._species = value

    def set_weight(self, value):
        self._weight = value

    def get_weight(self):
        return self._weight

    def get_species(self):
        return self._species

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
generic_animal = ZooAnimal("ass", "ass")
print(generic_animal.get_species())
generic_animal.sound()
generic_animal.set_species("man")
print(generic_animal.get_species())

# Лев
lion = Lion(None, None)

lion.set_weight("123")
lion.set_species("Nikita")

lion.get_weight()
lion.get_species()
lion.roar()
lion.sound()

