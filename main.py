# Завдання 2
class Car:
    def __init__(self, make=None, model=None, year=None):
        self.make = make
        self.year = year
        self.model = model

    def get_info(self):
        return f"Рік випуску:{self.year}, Марка:{self.make}, Модель:{self.model}"


car_1 = Car("Tesla", "X", 2015)
print(car_1.get_info())


# Завдання 3

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_salary_info(self):
        return f"Заробітна плата {self.name}: заробітна плата - {self.salary}, посада - {self.position}"


employee_1 = Employee("Bohdan", "director", 55000)

print(employee_1.get_salary_info())

# Завдання 4

class Rectangle:

    def __init__(self, width=None, height=None):
        self.width = width
        self.height = height

    def calculate_area(self):
        return f"Площа = {int(self.width) * int(self.height)}"

    def calculate_perimeter(self):
        return f"Периметр = {(int(self.width) + int(self.height)) * 2}"

rectangle_1 = Rectangle(7, 8)
print(rectangle_1.calculate_area(), rectangle_1.calculate_perimeter())


# Завдання 5

class Product:

    def __init__(self,  name=None, price=None, quantity=None):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        result = int(self.price) * int(self.quantity)
        return f"Загальна вартість: {result}"

    def display_info(self):
        return f"Назва товару: {self.name}, ціна за 1 штуку: {self.price}, кількість товару: {self.quantity}"


product_1 = Product("apple", "20", "7")

print(product_1.display_info(), product_1.calculate_total_price())
