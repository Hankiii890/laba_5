class User:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address =address

class Product:
    def __init__(self, name, prise, description):
        self.name = name
        self.prise = prise #Цена продукта
        self.description = description #Описание продукта

class Order:# Заказ
    def __init__(self, user, product, quantity):
        self.user = user
        self.product = product
        self.quantity = quantity # Кол-во
        self.total_prise = product.prise * quantity #Общая цена

    def display_order(self):
        print("{} ordered {} {} for ${}".format(self.user.name, self.quantity, self.product.name, self.total_prise))

user1 = User("John Doe", "jdoe@example.com", "123 Main St")
product1 = Product("Apple AirPods", 159.00, "Bluetooth headphones")
order1 = Order(user1, product1, 2)
order1.display_order()
