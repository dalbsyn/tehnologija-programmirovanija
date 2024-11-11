class Vehicle:
    def __init__(self, _make, _model, _year):
        self._make = _make
        self._model = _model
        self._year = _year

    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def get_year(self):
        return self._year

    def set_make(self, value):
        self._make = _make

    def set_model(self):
        self._make = _make

    def get_year(self):
        self._year = _year
    
class Car(Vehicle):
    def play_music(self):
        print("ИГРАЮ МУЗЫКУ")

class Truck(Vehicle):
    def load_cargo(self):
        print("ЗАГРУЖАЮ ГРУЗ")


honda = Vehicle(None, None, None)

print(honda.get_year)
