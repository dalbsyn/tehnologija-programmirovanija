# 5 вариант
class Product:
    def __init__(name,price,quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self.__name = name

    def get_price(self):
        return self._price

    def set_price(self,price):
        self.__price = price

    def get_quantity(self):
        return self._quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity

class Electronics(Product):
    def apply_warranty(self)

    def get_product_details()
        self.apply_warranty()

class Clothing(Product):
    def size(self)

    def get_product_details()
        self.size()

class Grocery(Product):
    def check_expiry_date(self)

    def get_product_details()
        self.check_expiry_date()
