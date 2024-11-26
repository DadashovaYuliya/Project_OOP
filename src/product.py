from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Метод сложения двух товаров (произведение цены на количество), при условии нахождения товара в одном классе"""
        if type(other) is self.__class__:
            result = (self.price * self.quantity) + (other.price * other.quantity)
            return result
        raise TypeError

    @classmethod
    def new_product(cls, prod_param: dict):
        """Метод, принимающий на вход параметры товара в словаре и возвращает созданный объект класса"""
        name = prod_param["name"]
        description = prod_param["description"]
        price = prod_param["price"]
        quantity = prod_param["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: int):
        """Изменение цены, если она соответствует условиям"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        elif new_price < self.__price:
            user_input = input('Цена товара уменьшилась. Введите "y", чтобы понизить цену:\n')
            if user_input.lower() == "y":
                self.__price = new_price
        else:
            self.__price = new_price
