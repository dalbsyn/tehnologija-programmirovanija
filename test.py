1 Вариант
class Pet:
   def __init__(self, name, age):
       self.__name = name
       self.__age = age
    
   def get_name(self):
       return self.__name
    
   def get_age(self):
       return self.__age

   def set_name(self, name):
       self.__name = name

   def set_age(self, age):
       self.__age = age

   def make_sound(self):

class Dog(Pet):
   def bark(self):
       print("Гав")

class Cat(Pet):
   def meow(self):
       print("Мяу")

class Bird(Pet):
   def chirp(self):
       print ("пчирик")
       