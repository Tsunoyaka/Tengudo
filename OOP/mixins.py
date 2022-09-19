""" Миксины """

# Mixin - классы, которые используются для дополнения функционала других классов путем наследования
# От миксинов нельзя создавать объекты

# class MicrowaveMixin:
#     def heat(self):
#         print('Грею еду')


# class Fridge:
#     def cold(self):
#         print('Охлаждаю кухню')


# class TV:
#     def watch_tv(self):
#         print('передаю шоу')


# class Cooker:
#     def cook(self):
#         print('Готовю еду')



# class Kitchen(MicrowaveMixin, TV, Cooker, Fridge):
#     p = 10


# r = Kitchen()


class BaseClass:
    def eat(self):
        pass


class BaseMixin:
    def eat(self):
        print('Я много ем')


class ChildrenClass(BaseMixin, BaseClass):
    pass


obj = ChildrenClass()
obj.eat()

# При наследовании от миксинов и других классов - миксины нужно указывать в первую очередь (MRO)