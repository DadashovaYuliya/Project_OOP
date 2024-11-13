from src.product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        sum_quantity = 0
        for prod in self.__products:
            sum_quantity += prod.quantity
        return f"{self.name}, количество продуктов: {sum_quantity} шт."

    @property
    def products(self):
        """Метод для вывода списка товаров в формате строки"""
        products_str = ""
        for prod in self.__products:
            products_str += f"{str(prod)}\n"
        return products_str

    @property
    def products_list(self):
        return self.__products

    def add_product(self, product: Product):
        """Метод для добавления продукта в атрибут products"""
        self.__products.append(product)
        Category.product_count += 1
