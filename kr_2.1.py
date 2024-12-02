2 вариант
class Infrastructure:
   def __init__(self, name):
       self.name = name

   def __str__(self):
       return f"Инфраструктура: {self.name}"

class Road(Infrastructure):
   def __init__(self, name, length):
       super().__init__(name)
       self.length = length

   def __str__(self):
       return f"Дорога: {self.name}, Длина: {self.length}"

class Building(Infrastructure):
   def __init__(self, name, floars):
       super().__init__(name)
       self.floars = floars
       return f"Здание: {self.name}, Высота: {self.height}"

class Park(Infrastructure):
   def __init__(self, name, area):
       super().__init__(name)
       self.area = area
def __str__(self):
       return f"Парк: {self.name}, Площадь: {self.area} "

class City:
   def __init__(self, name):
       self.name = name
       self.infrastructure = []

   def add_infrastructure(self, obj):
       if isinstance(obj, Infrastructure):
       self.infrastructure.append(obj)
       return f"Обьект: должен быть наследником класса Infrastructure.")
 
   def list_infrastructure(self):
       if not self.infrastructure:
       print(f"В городе {self.name} нет объектов инфраструктуры.")
       else:
       for obj in self.infrastructure:
       print(obj)

   def __del__(self):
       print(f"Город {self.name} и все его инфраструктурные элементы удалены.")
       self.infrastructure.clear()





