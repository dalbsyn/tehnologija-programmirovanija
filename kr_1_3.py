# 3 variant
# Инкапсуляция
class Student:
    def __init__(self, name, grades):
        self.__name = name
        self.__grades = grades

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_grades(self):
        return self.__grades

    def set_grades(self, grades):
        self.__grades = grades

    def add_grade(grade):
         return grade.add_grade

    def get_average_grade():
         return grade.get_average_grade

    def get_name(self):
         return self.__name

    def student(self):
        pass

    def student(grade):
        pass


# Наследники
class Shape():
    def get_area(self):
        print("")

    def get_area(self):
        self.get_area()

    def get_area(self):
        return 0

class Rectangle():
    def get_area(self):
        print("Возвращает площадь прямоугольника")

    def get_area(self):
        self.width()

def get_area(self):
        self.height()

class Circle():
    def get_area(self):
        print("Возвращает площадь круга")

    def radius(self):
        self.radius()


# Полиморфизм
piano = play("Piano is playing a melody.")
guitar = play("Guitar is strumming chords.")
drum = play("Drum is beating a rhythm")

Instrument = [piano, guitar,drum]

for instrument in instruments:
    instrument.play()