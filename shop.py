from classes.products import Electronics, Clothing, Housechemicals
from classes.users import Customer, Admin
from classes.shoping_carts import ShoppingCart


# Создаем продукты
laptop = Electronics(name="Ноутбук", price=120000, brand="Dell", warranty_period=2)
tshirt = Clothing(name="Футболка", price=200, size="M", material="Хлопок")
Housechemicals = Housechemicals ('Гель для посуды', 370.0, '5 литров', '24 месяца')

# Создаем пользователей
customer = Customer(username="Mikhail", email="python@derkunov.ru", address="033 Russ Bur")
admin = Admin(username="root", email="root@derkunov.ru", admin_level=5)

# Создаем корзину покупок и добавляем товары
cart = ShoppingCart(customer)
cart.add_item(laptop, 1)
cart.add_item(tshirt, 3)
cart.add_item(Housechemicals, 3)

#Регистрация корзины
#cart.register(admin)

# Выводим детали корзины
print(cart.get_details())

