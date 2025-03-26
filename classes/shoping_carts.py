# 3. Класс для управления корзиной покупок

class ShoppingCart:
    """
    Класс, представляющий корзину покупок.
    добавлены атрибутыЖ
     - покупатель (имя покупателя)
     - администратор зарегистрировавший покупки (и метод для регистрации
     - фраза по  умолчанию покупки не зарегистрированы
    """
    def __init__(self, customer):
        self.items = []
        self.customer =customer
        self.admin = None
        self.cartreg = "Покупки не зарегистрированы"

    def add_item(self, product, quantity):
        """
        Добавляет продукт в корзину.
        """
        self.items.append({"Продукт": product, "количество": quantity})

    def register(self, admin):
       """
       Регистрация корзины администратором
       """
       self.admin = admin


    def remove_item(self, product_name):
        """
        Удаляет продукт из корзины по имени.
        """
        self.items = [item for item in self.items if item["Продукт"].name != product_name]

    def get_total(self):
        """
        Возвращает общую стоимость продуктов в корзине.
        """
        total = sum(item["Продукт"].price * item["количество"] for item in self.items)
        return total

    def get_details(self):
        """
        Возвращает детализированную информацию:
         1 Полное имя покупателя.
         2 Содержимое корзины и общая стоимость.
         3 администратор зарегистрировавший корзину
        """
        title = "Корзина покупок. "
        customer = "Покупатель "  + "Имя: " + self.customer.username +" Почта: " + self.customer.email + '\n'
        if self.admin is not None:
            self.cartreg = "Покупки зарегистрировал Администратор: " + self.admin.username + " Почта: " + self.admin.email
        details = f"{title} {customer}"
        for item in self.items:
            details += f"{item['Продукт'].get_details()}, Количество: {item['количество']}\n"
        details += f'Общая сумма: {self.get_total()} руб.\n'
        details += f"{self.cartreg}"
        return details