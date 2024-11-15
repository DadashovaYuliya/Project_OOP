class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, prod_param: dict):
        '''Метод, принимающий на вход параметры товара в словаре и возвращает созданный объект класса'''
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
        '''Изменение цены, если она соответствует условиям'''
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        elif new_price < self.__price:
            user_input = input('Цена товара уменьшилась. Введите "y", чтобы понизить цену:\n')
            if user_input.lower() == "y":
                self.__price = new_price
        else:
            self.__price = new_price
