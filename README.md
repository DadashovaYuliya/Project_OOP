# Домашняя работа 14.1

## Описание:

Созданы классы: Product и Category.
Для класса Category добавлены два атрибута класса: количество категорий (category_count) 
и количество товаров (product_count).

## Установка:

1. Клонируйте репозиторий:
```
git@github.com:DadashovaYuliya/Project_OOP.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Использование функций:

1. Модуль utils: реализована функция для создания объектов класса из файла json.

## Классы и их методы

1. Реализованы родительские классы (Product, Category). 
2. Реализованы дочерние классы к классу Product (Smartphone, LawnGrass).
3. Для класса Category реализованы методы:
- для вывода списка товаров в формате строки
- для добавления продукта в атрибут products
4. Для класса Product реализованы методы:
- сложения двух товаров (произведение цены на количество), при условии нахождения товара в одном классе
- изменения цены, если она соответствует условиям


## Тестирование:
Для модулей category.py, product.py, lawn_grass.py, smartphone.py реализованы тесты:
```
Name                       Stmts   Miss  Cover
------------------------------------------------
src\__init__.py                 0      0   100%
src\category.py                32      0   100%
src\lawn_grass_product.py       7      0   100%
src\product.py                 37      3    92%
src\product_iterator.py        13      2    85%
src\smartphone_product.py       8      0   100%
tests\__init__.py               0      0   100%
tests\conftest.py              39      1    97%
tests\test_category.py         25      0   100%
tests\test_lawn_grass.py       21      0   100%
tests\test_product.py          31      0   100%
tests\test_smartphone.py       23      0   100%
-----------------------------------------------
TOTAL                         236      6    97%
