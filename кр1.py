#3 Вариант
#1 Инкапсуляция
from pyclbr import Class


Class Vehicle:
   def init(self, _make, _model, _year):
     self._make= make
     self._model= model
     self._year= year
   def get_make(self):
       return self._make
   def set_make(self,make):
      self._make= make
   def get_model(self):
       return self._model
   def set_vodel(self,model):
      self._model= model
   def get_year(self):
       return self._year
   def set_year(self,year):
      self._year= year
#2 Наследование
Class Car(Vehicle):
    def play_music(self):
        print("Играет музыка")
    
    def use(self):
        print("Машина играет музыку")

Class Truck(Vehicle):
    def load_cargo(self):
        print("Грузит груз")
    
    def use(self):
        print("Грузовик грузит груз")


