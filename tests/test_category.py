from tests.conftest import product1, product2, product3


def test_category_init(category1):
    assert category1.name == 'Смартфоны'
    assert category1.description == 'Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни'
    assert category1.products_list == [product1, product2, product3]

    assert category1.category_count == 1
    assert category1.product_count == 3


def test_products_str(category1):
    assert category1.products == ('Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                  'Iphone 15, 210000.0 руб. Остаток: 8 шт.\n'
                                  'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n')


def test_add_product(category1, product4):
    assert len(category1.products_list) == 3
    category1.products.add_product(product4)
    assert len(category1.products_list) == 4
