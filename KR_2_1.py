#4 вариант

class Animal:
    def __init__(self, herbivore, carnivore, nocturnal):
        self.herbivore = herbivore
        self.carnivore = carnivore
        self.nocturnal = nocturnal

    def __repr__(self):
         return f"Animal(herbivore = '{self.herbivore}', carnivore = '{self.carnivore}', nocturnal = '{self.nocturnal})"

class Zoo:
    def __init__(self):
        self.animals = {}


    @abc
    def create_animal(herbivore, carnivore, nocturnal) -> Animal:
        return Animal(herbivore, carnivore, nocturnal)

#Пример использования
 if __name__ == "__main__":
      zoo = Zoo()

      animal1 = Zoo.create_animal("Зебра")
      animal2 = Zoo.create_animal("Тигр")
      animal3 = Zoo.create_animal("Сова")





