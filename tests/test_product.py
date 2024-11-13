from src.product import Product


def test_product_init(product1, product2, product3):
    assert product1.name == 'Samsung Galaxy S23 Ultra'
    assert product1.description == '256GB, Серый цвет, 200MP камера'
    assert product1.price == 180000.0
    assert product1.quantity == 5

    assert product2.name == 'Iphone 15'
    assert product2.description == '512GB, Gray space'
    assert product2.price == 210000.0
    assert product2.quantity == 8

    assert product3.name == 'Xiaomi Redmi Note 11'
    assert product3.description == '1024GB, Синий'
    assert product3.price == 31000.0
    assert product3.quantity == 14


def test_new_product():
    product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    product.name = "Samsung Galaxy S23 Ultra"
    product.description = "256GB, Серый цвет, 200MP камера"
    product.price = 180000.0
    product.quantity = 5


def test_new_price(capsys):
    product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == 'Цена не должна быть нулевая или отрицательная'
    product.price = 200000.0
    assert product.price == 200000.0


def test_product_str(product1):
    assert str(product1) == 'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.'


def test_product_add(product1, product2):
    assert product1 + product2 == 2580000.0
