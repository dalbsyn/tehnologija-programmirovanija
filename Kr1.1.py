#Вариант 1
class Vehicle:
   def __init__(self, speed, color):
    self._speed = speed
    self._color = color

   def get_speed():
      return self._speed

   def set_speed():
     if speed < 0:
      print("скорость не может быть отрицательной")
      self._speed=speed

   def get_color():
    return self._color

   def set_color():
    self._color=color

class Car(Vehicle):
   def drive():
       print("Машина едет")
   def move(self):
       print("Машина двигается")
       
class Bike(Vehicle):
   def pedal():
       print("Велосипед крутит педали")
   def move():
       print("Велосипед едет")
       
class Boat(Vehicle):
   def sail():
       print("Лодка плывёт")
   def move():   
       print("Лодка плывёт")