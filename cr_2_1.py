# 1 игрок и команда

class Player:
    def __init__(self, age):
        self.age = age


class Team:
    def __init__(self, age):
        self.age = age
        self.spisok = []
    
    def add_in_team(self, age):
        return self.spisok.append(age)

    def del_in_team(self, element):
        return self.spisok.remove(element)

    def cred_chislo(self):
        summ = 0
        for i in self.sposok:
            summ += age.i
        print(summ)

# 2 барбара

class Player:
    def __init__(self, age):
        self.age = age

class FieldPlayer:
    def __init__(self, age, weight):
        super().__init__(age)
        self.weight = weight

class Goalkeep:
    def __init__(self, age, weight):
        super().__init__(age)
        self.weight = weight

class Team:
    def __init__(self, age):
        super().__init__(age)
        self.spisok = []

    def add_player(self, element):
        self.spisok.append(element)

    def cred_chislo(self):
        summ = 0
        for i in self.spisok:
            summ += age.i
        print(summ)

player1 = Player()
player1.add_player(11)


