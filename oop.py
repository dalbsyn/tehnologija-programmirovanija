class Employee():
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def get_name(self):
        return self._name
    def get_salary(self):
        return self._salary

    def set_salary(self, salary):
        self._salary = salary

    def c_bonus(self):
        return 500

class Manager(Employee):
    def c_bonus(self):
        return self._salary * 0.1
class Engineer(Employee):
    def c_bonus(self):
        return self._salary * 0.5
class Intern(Employee):
    def c_bonus(self):
        return self._salary * 0.9

zp_managera = Manager("Sonya", 100000)
zp_enginera = Engineer("Nasty", 200000)
zp_interna = Intern("Ara", 10000)

print(zp_managera.c_bonus())
print(zp_enginera.c_bonus())
print(zp_interna.c_bonus())

