from tests.conftest import product1, product2, product3


def test_category_init(category1, category_2):
    assert category1.name == 'Смартфоны'
    assert category1.description == '''
    Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни
    '''
    assert category1.products == [product1, product2, product3]

    assert category_2.name == 'Фрукты'
    assert category_2.description == 'Плодовые культуры'
    assert category_2.products == ['Яблоко', 'Груша']

    assert category1.category_count == 2
    assert category1.product_count == 5

    assert category_2.category_count == 2
    assert category_2.product_count == 5
