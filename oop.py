class Employee():
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def get_name(self):
        return self._name
    def get_salary(self):
        return self._salary

    def set_name(self, name):
        return self._name
    def set_salary(self, salary):
        return self._salary

    def c_bonus(self, salary):
        return self._salary

    class Manager(Employee):
        def c_bonus(self, salary):
            return self._salary * 0.1
    class Engineer(Employee):
        def c_bonus(self, salary):
            return self._salary * 0.5
    class Intern(self, salary):
        def c_bonus(self, salary):
            return self._salary * 0.9

zp_managera = Employee("Sonya", 100000)
zp_enginera = Employee("Nasty", 200000)
zp_interna = Employee("Ara", 10000)

print(c_bonus.zp_managera)
print(c_bonus.zp_enginera)
print(c_bonus.zp_interna)

