class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            products = file.read()  # Читаем содержимое файла
        return products  # Возвращаем содержимое файла

    def add(self, *products):
        existing_products = set()
        try:
            # Загружаем существующие продукты для проверки на дубликаты
            with open(self.__file_name, 'r') as file:
                existing_products = {line.split(',')[0].strip() for line in file.readlines()}
        except FileNotFoundError:
            pass  # Если файла нет, просто продолжаем
        for product in products:
            if product.name in existing_products:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                with open(self.__file_name, 'a') as file:
                    file.write(f'{product}\n')  # добавляем новый продукт в файл


# Пример работы программы
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # вывод для проверки метода __str__

s1.add(p1, p2, p3)  # добавление продуктов

print(s1.get_products())  # считает и выводит все продукты из файла
