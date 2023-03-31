#Single Responsibility Principle
#Принцип единственной Обязательности
class Car:
    def __init__(self, Machine_brand: str):
        self.Mashine_brand = brand

    def get_name(self):
        pass

class UserDB:
    def get_brand(self, id) -> Car:
        pass
    def preservation(self, car: Car):
        pass

#Open - Closed Principle
#Принцип открытости / закрытости
class Employee:
    def __init__(self,name):
        self.name = name

    def get_info(self):
        return f"{self.name} is an employee"

class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

    def get_info(self):
        return f"{self.name} leads department {self.department}"

#Liskov Substitution Principle
#Принцип подстановки листов      !!!производные классы должны заменять свои базовые классы, не вызывая ошибок.
from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def notify(self, message, email):
        pass


class Email(Notification):
    def notify(self, message, email):
        print(f'Send {message} to {email}')


class SMS(Notification):
    def notify(self, message, phone):
        print(f'Send {message} to {phone}')


if __name__ == '__main__':
    notification = SMS()
    notification.notify('Hello', 'john@test.com')

#Interface Segregation Principle
#Принцип разделения интерфейсов
class Bird(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def do_sound(self) -> str:
        pass


class FlyingBird(Bird):

    @abstractmethod
    def fly(self):
        pass


class SwimmingBird(Bird):

    @abstractmethod
    def swim(self):
        pass


class Crow(FlyingBird):

    def fly(self):
        print(f"{self.name} is flying high and fast!")

    def do_sound(self) -> str:
        return "Caw"


class Duck(SwimmingBird, FlyingBird):

    def fly(self):
        print(f"{self.name} is flying not very high")

    def swim(self):
        print(f"{self.name} swims in the lake and quacks")

    def do_sound(self) -> str:
        return "Quack"

#Dependecy Inversion Principle
#Принцип инверсии зависимостей
from abc import ABC


class CurrencyConverter(ABC):
    def convert(self, from_currency, to_currency, amount) -> float:
        pass


class FXConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount) -> float:
        print('Converting currency using FX API')
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 1.15


class AlphaConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount) -> float:
        print('Converting currency using Alpha API')
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 1.2


class App:
    def __init__(self, converter: CurrencyConverter):
        self.converter = converter

    def start(self):
        self.converter.convert('EUR', 'USD', 100)


if __name__ == '__main__':
    converter = AlphaConverter()
    app = App(converter)
    app.start()











