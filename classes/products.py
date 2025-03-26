# 1. Базовый класс Product и производные классы для различных типов продуктов

class Product:
    """
    Базовый класс, представляющий продукт.
    """
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_details(self):
        return f"Продукт: {self.name}, Цера: {self.price} руб."

class Electronics(Product):
    """
    Класс, представляющий электронный продукт, наследующий класс Product.
    """
    def __init__(self, name, price, brand, warranty_period):
        super().__init__(name, price)
        self.brand = brand
        self.warranty_period = warranty_period

    def get_details(self):
        return f"Электроника: {self.name}, Бренд: {self.brand}, Цена: {self.price} руб, Гарантия: {self.warranty_period} лет"

class Clothing(Product):
    """
    Класс, представляющий одежду, наследующий класс Product.
    """
    def __init__(self, name, price, size, material):
        super().__init__(name, price)
        self.size = size
        self.material = material

    def get_details(self):
        return f"Одежда: {self.name}, Размер: {self.size}, Материал: {self.material}, Цена: {self.price} руб."

class Housechemicals(Product):
    """
    Класс, представляющий бытовую химию, наследующий класс Product.
    К наименованию и цене добавлено
    Назначение (Средства для стирки, Чистящие и моющие средства, Средства для мытья посуды и т.п.).
    Срок годности.
    Бренд убран.
    """
    def __init__(self, name, price, packaging, expiration_date):
        super().__init__(name, price)
        self.packaging = packaging
        self.expiration_date = expiration_date
    def get_details(self):
        return f"Бытовая химия: {self.name}, Упаковка: {self.packaging}, Срок годности: {self.expiration_date} Цена: {self.price} руб."



