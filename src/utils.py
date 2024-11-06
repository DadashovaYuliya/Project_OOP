import json
import os

from src.category import Category
from src.product import Product


def read_json(path: str) -> dict:
    """Функция для чтения файла формата json"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data):
    """Функция для создания объектов класса из файла формата json"""
    category_list = []
    for cat in data:
        product_list = []
        for prod in cat["products"]:
            product_list.append(Product(**prod))
        cat["products"] = product_list
        category_list.append(Category(**cat))

    return category_list


if __name__ == "__main__":
    raw_data = read_json("../data/products.json")
    objects = create_objects_from_json(raw_data)
    print(objects[0].name)
    print(objects[0].products)
    print(objects[1].name)
    print(objects[1].products)
