# 5 вариант
class Product:
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity


class Electronics(Product):
    def apply_warranty(self):
        print("Гарантия на электронику применена.")

    def get_product_details(self):
        self.apply_warranty()
        print(f"Название: {self.get_name()}, Цена: {self.get_price()}, Количество: {self.get_quantity()}")


class Clothing(Product):
    def size(self):
        print("Размер одежды указан.")

    def get_product_details(self):
        self.size()
        print(f"Название: {self.get_name()}, Цена: {self.get_price()}, Количество: {self.get_quantity()}")


class Grocery(Product):
    def check_expiry_date(self):
        print("Проверка срока годности.")

    def get_product_details(self):
        self.check_expiry_date()
        print(f"Название: {self.get_name()}, Цена: {self.get_price()}, Количество: {self.get_quantity()}")


if __name__ == "__main__":
    electronics = Electronics("Телевизор", 30000, 5)
    electronics.get_product_details()

    clothing = Clothing("Футболка", 1500, 10)
    clothing.get_product_details()

    grocery = Grocery("Молоко", 200, 20)
    grocery.get_product_details()
