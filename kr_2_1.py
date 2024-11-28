#1 Вариант
#1
class University:
    def __init__(self):
        class University:
    def __init__(self):
        self._departments = []

    def add_department(self, department):
        if department not in self._departments:
            self._departments.append(department)

    def get_departments(self):
        return self._departments

    def __init__(self):
        return f"Университет с факультетами: {[dept.name for dept in self._departments]}"
dept1 = Department("ФИТ")
dept2 = Department("ФЭАТ")
dept3 = Department("Э")

university = University()
university.add_department(dept1)
university.add_department(dept2)


print(university)
print("Список факультетов в университете:")
for dept in university.get_departments():
    print(dept)

   

#2
class University:
     def __init__(self):
      print("Название университета")
     def __init__(self):
      print("Год основания")
     def __init__(self):
      print("Основные сведения об университете")
class FacultyManager:
     def __init__(self):
      print("Добавление факультетов")
     def __init__(self):
      print("Удаление факультетов")
     def __init__(self):
      print("Вывод списка факультетов")




