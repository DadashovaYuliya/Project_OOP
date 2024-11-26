import pytest

from src.product import Product
from tests.conftest import product1, product2, product3


def test_category_init(category1, product1, product2, product3):
    assert category1.name == 'Смартфоны'
    assert category1.description == 'Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни'
    assert category1.products_list == [product1, product2, product3]

    assert category1.category_count == 1
    assert category1.product_count == 3


def test_products_str(category1):
    assert category1.products == ('Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                  'Iphone 15, 210000.0 руб. Остаток: 8 шт.\n'
                                  'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n')


def test_add_product(category1, smartphone1, product_error):
    assert len(category1.products_list) == 3
    category1.add_product(smartphone1)
    assert len(category1.products_list) == 4
    with pytest.raises(TypeError):
        category1.add_product(product_error)


def test_category_str(category1):
    assert str(category1) == 'Смартфоны, количество продуктов: 27 шт.'


def test_product_iterator(product_iterator):
    assert product_iterator.index == 0
    assert next(product_iterator).name == 'Samsung Galaxy S23 Ultra'
    assert next(product_iterator).name == 'Iphone 15'
    assert next(product_iterator).name == 'Xiaomi Redmi Note 11'

    with pytest.raises(StopIteration):
        next(product_iterator)


def test_middle_price(category1, category_without_product):
    assert category1.middle_price() == 140333.33
    assert category_without_product.middle_price() == 0


def test_custom_exception(capsys, category1):
    assert len(category1.products_list) == 3

    product_add = Product('Xiaomi', '1024GB, Красный', 35000.0, 2)
    category1.add_product(product_add)
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-2] == 'Продукт успешно добавлен'
    assert message.out.strip().split('\n')[-1] == 'Обработка добавления товара завершена'

    assert len(category1.products_list) == 4
