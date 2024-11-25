#3 вариант

class Player:
    def__init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age 
        

class FieldPlayer(Player):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position


class Goalkeeper(Player):
    def __init__(self, name, age, reflexes):
        super().__init__(name, age)
        self.reflexes = reflexes

class Team:
    def__init__(self, name):
        self.__name = name
        self.player = []

    def add_player(self, player:Player):
        self.players.append(player)

    def remove_player(self, player: Player):
        if player in self.players:
            self.players.remove(player)

        
