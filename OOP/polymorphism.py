""" Полиморфизм """

# Полиморфизм - принцип ООП, которой заключается в использовании
# одной сущности(метод, оператор) для различных типов объектов.

# +
from mimetypes import init


num1 = 10
num2 = 30
# print(num1 + num2) # сложение - 40

str1 = "Hello"
str2 = 'World'
# print(str1 + str2) # конкатенация - HelloWorld


# class A:
#     def method1(self):
#         return 10 + 10

# class B:
#     def method1(self):
#         return 'method1'

# objA = A()
# objB = B()
# for obj in (objA, objB):
#     obj.method1()



# class Cat:
#     def meow(self):
#         print('meow')

# class Dog:
#     def bark(self):
#         print('bark')




# cat1 = Cat()
# dog1 = Dog()
# for animal in (cat1, dog1):
#     if type(animal) is Cat:
#         animal.meow()
#     else:
#         animal.bark()



""" Абстракция """

# Абстракция - сущность без конкретной реализации



class Animal:
    def __init__(self, sound, eat, move) -> None:
        self.sound() 
        self.eat()
        self.move()

    def eat(self):
        raise NotImplementedError(self.__class__.__name__)

    def sound(self):
        raise NotImplementedError(self.__class__.__name__)

    def move(self):
        raise NotImplementedError(self.__class__.__name__)



from abc import ABC, abstractmethod


class AbstractClass(ABC):
    def get_x(self):
        return 'x'

    @abstractmethod
    def abs_method(self):
        pass


class ConcreteClass(AbstractClass):
    def method1(self):
        print(123123)

    def abs_method(self):
        return 'Hello World'


obj = ConcreteClass()


