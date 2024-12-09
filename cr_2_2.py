# вариант 3
# 1 задание
class Team:
    def __init__(self):
        self.spisok = []

    def add_element(self, element):
        self.spisok.append(element)

    def del_element(self, element):
        self.spisok.remove(element)
    
    def cred_chilso(self, element):
        summ = 0
        for i in self.spisok:
            summ += i.age
        print(summ / 2)

class Player:
    def __init__(self, age):
        self.age = age

player = Player(20)
player1 = Player(40)

team = Team()

team.add_element(player)
team.add_element(player1)

team.del_element(player1)


# 2 задание

class Player:
    def __init__(self, age):
        self.age = age

class FieldPlaywer(Player):
    def __init__(self, age, weight):
        super().__init__(age)
        self.weight = weight


class Goalkeper(Player):
    def __init__(self, age, weight):
        super().__init__(age)
        self.weight = weight

class Team:
    def __init__(self)
        self.spisok = []

    def add_element(self, element):
        self.spisok.append(element)

    def del_element(self, element):
        self,spisok.remove(element)

    def sred_chislo(self):
        summ = 0
        for i in self.spisok:
            summ += i.age
        print(summ / 2)

