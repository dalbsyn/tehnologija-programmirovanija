class Product:
   def __init__(self, name, price, quantity):
       self.__name = name
       self.__price = price
       self.__quantity = quantity

   def get_name(self):
       return self.__name

   def get_price(self):
       return self.__price

   def get_quantity(self):
       return self.__quantity

   def set_name(self, name):
       self.__name = name

   def set_price(self, price):
       self.__price = price

   def set_quantity(self, quantity):
       self.__quantity = quantity

   def get_product_details(self):
       return f"Name: {self.__name}, Price: {self.__price}, Quantity: {self.__quantity}"

class Electronics(Product):
   def apply_warranty(self):
       print("Электроника ")

   def check_expiry_date(self):
       print("Гарантия на электронику ")

class Clothing(Product):
   def apply_warranty(self):
       print("Одежда ")

   def check_expiry_date(self):
       print("Одежда не имеет срока годности")

class Grocery(Product):
   def apply_warranty(self):
       print("Продукты питания ")

   def check_expiry_date(self):
       print("Продукты имеют срок годности")
