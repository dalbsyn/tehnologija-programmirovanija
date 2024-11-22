# 2 вариант

'''
1 задание - начало.
'''

class Book:
    def __init__(self, title, author, available:bool):
        self.__title = title
        self.__author = author 
        self.__available = available

    def get_title(self):
        return self.__title 

    def get_author(self):
        return self.__author

    def get_available(self):
        return self.__avaiable

    def set_title(self, value):
        self.__title = value

    def set_author(self, value):
        self.__author = value

    def set_available(self):
        self.__avaiable = value

    def borrow(self):
        self.__available = False

    def borrow(self):
        self.__available = True

    def get_info(self):
        print("Заголовок: {0};\nАвтор: {1};\nДоступен: {2}.".format(self.__title, self.__author, self.__available))

book_1 = Book("no", "vadim", False)
book_1.get_info()
book_1.borrow()
book_1.get_info()

'''
1 задание - конец.
2 задание - начало.
'''

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_name(self):
        return self.name

    def get_position(self):
        return self.position

    def get_salary(self):
        return self.salary

    def set_name(self, value):
        self.name = name

    def set_position(self, value):
        self.position = value

    def set_salary(self, value):
        self.salary = value

    def get_info(self):
        print("Имя: {0};\nДолжность:{1};\nЗарплата:{2}".format(self.name, self.position, self.salary))


class Manager(Employee):
    def __init__(self, department):
        self.department = department


    def get_department(self):
        return self.department

    def set_name(self, value):
        self.department = department


class Developer(Employee):
    def __init__(self, department):
        self.programming_language = programming_language


    def get_department(self):
        return self.programming_language

    def set_name(self, value):
        self.programming_language = programming_language

'''
2 задание - конец.
3 задание - начало
'''

class Device:
    def turn_on(self):
        print("ON")


class Phone:
    def turn_on(self):
        print("Phone is now on")


class Laptop:
    def turn_on(self):
        print("Laptop is booting up")


class Device:
    def turn_on(self):
        print("Tablet is ready to use")

'''
3 задание - конец.
'''
