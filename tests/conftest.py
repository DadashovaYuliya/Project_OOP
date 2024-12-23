import pytest

from src.category import Category
from src.lawn_grass_product import LawnGrass
from src.product import Product
from src.product_iterator import ProductIterator
from src.smartphone_product import Smartphone


@pytest.fixture
def product1():
    return Product('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)


@pytest.fixture
def product2():
    return Product('Iphone 15', '512GB, Gray space', 210000.0, 8)


@pytest.fixture
def product3():
    return Product('Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, 14)


@pytest.fixture
def category1(product1, product2, product3):
    return Category('Смартфоны',
                    'Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни',
                    [product1, product2, product3])


@pytest.fixture
def product4():
    return Product('Xiaomi', '1024GB, Красный', 35000.0, 2)


@pytest.fixture
def product_iterator(category1):
    return ProductIterator(category1)


@pytest.fixture
def smartphone1():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                         "S23 Ultra", 256, "Серый")


@pytest.fixture
def smartphone2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def lawn_grass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawn_grass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def product_error():
    return 'Трава'


@pytest.fixture
def category_without_product():
    return Category('Пустая','Без товаров',[])
