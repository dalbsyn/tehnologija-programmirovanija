#2 вариант
class Infrastructure:
    def __init__(self, name):
        self.name = name

    def get_info(self):
        return self.name

class Road(Infrastructure):
    pass


class Building(Infrastructure):
    pass


class Park(Infrastructure):
    pass

class City:
    def __init__(self):
        self.infrastructure = infrastructure

    def add_infrastructure(self, item):
        self.infrastructure.append(item)

    def remove_infrastructure(self, item):
        if item in self.infrastructure:
            self.infrastructure.remove(item)

    def list_infrastructure(self):
        return [item.get_info() for item in self.infrastructure]

city = City()
road = Road("Main Street")
building = Building("Town Hall")
park = Park("Central Park")

city.add_infrastructure(road)
city.add_infrastructure(building)
city.add_infrastructure(park)

print("City infrastructure:", city.list_infrastructure())
city.remove_infrastructure(road)
print("After removing road:", city.list_infrastructure())
