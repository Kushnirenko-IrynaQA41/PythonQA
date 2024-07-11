class SportResults:
    def __init__(self):
        self.points = 25

# Створення екземпляра класу
diving = SportResults()

# Виведення значення points
print(diving.points)  # Виведе 25

# Зміна значення points
diving.points = 150

# Повторне виведення значення points
print(diving.points)  # Виведе 150
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

# Створення екземпляра класу
el = Element('Silicium', 'Si', 14)

# Виведення значень атрибутів
print(el.name)    # Виведе 'Silicium'
print(el.symbol)  # Виведе 'Si'
print(el.number)  # Виведе 14

class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type

    def describe_shop(self):
        print(f"Shop Name: {self.shop_name}")
        print(f"Store Type: {self.store_type}")

    def open_shop(self):
        print("The online shop is open.")

# Створення екземпляра класу
store = Shop("Tech World", "Electronics")

# Виведення атрибутів
print(store.shop_name)  # Виведе 'Tech World'
print(store.store_type)  # Виведе 'Electronics'

# Виклик методів
store.describe_shop()
store.open_shop()
# Створення трьох різних екземплярів класу
store1 = Shop("Book Haven", "Books")
store2 = Shop("Fashion Fiesta", "Clothing")
store3 = Shop("Gadget Galaxy", "Gadgets")

# Виклик методу describe_shop() для кожного екземпляра
store1.describe_shop()
store2.describe_shop()
store3.describe_shop()
class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0

    def describe_shop(self):
        print(f"Shop Name: {self.shop_name}")
        print(f"Store Type: {self.store_type}")

    def open_shop(self):
        print("The online shop is open.")

    def set_number_of_units(self, number):
        self.number_of_units = number

    def increment_number_of_units(self, increment):
        self.number_of_units += increment

# Створення екземпляра класу
store = Shop("Tech World", "Electronics")

# Виведення значення number_of_units
print(store.number_of_units)  # Виведе 0

# Зміна та виведення значення number_of_units
store.number_of_units = 100
print(store.number_of_units)  # Виведе 100

# Виклик методу set_number_of_units()
store.set_number_of_units(200)
print(store.number_of_units)  # Виведе 200

# Виклик методу increment_number_of_units()
store.increment_number_of_units(50)
print(store.number_of_units)  # Виведе 250
