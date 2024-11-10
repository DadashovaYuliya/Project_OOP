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

    @property
    def products(self):
        '''Метод для вывода списка товаров в формате строки'''
        products_str = ""
        for prod in self.__products:
            products_str += f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.\n"
        return products_str

    @property
    def products_list(self):
        return self.__products

    def add_product(self, product: Product):
        '''Метод для добавления продукта в атрибут products'''
        self.__products.append(product)
        Category.product_count += 1
