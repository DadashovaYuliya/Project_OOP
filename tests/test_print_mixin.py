from src.lawn_grass_product import LawnGrass
from src.product import Product
from src.smartphone_product import Smartphone


def test_print_mixin(capsys):
    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    message = capsys.readouterr()
    assert message.out.strip() == 'Smartphone(Iphone 15, 512GB, Gray space, 210000.0, 8)'

    LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == 'LawnGrass(Газонная трава 2, Выносливая трава, 450.0, 15)'

    Product('Xiaomi', '1024GB, Красный', 35000.0, 2)
    message = capsys.readouterr()
    assert message.out.strip() == 'Product(Xiaomi, 1024GB, Красный, 35000.0, 2)'
