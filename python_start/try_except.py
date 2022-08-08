"""try excetp """

# try except - конструкция для обработки исключений

# исключение - проблема в логике работы кода

# ZeroDivisionError - ошибка деления на ноль
# print(10 / 0)


# NameError - исключения отсутствия имени
# a = 10
# b = 20
# print(c)


# AttributeError - ошибка атрибута
# string = 'word'
# string.get('o')


# KeyError - ошибка ключа
# dict_ = {'a':10, 'b': 20}
# dict_['c']


# IndexError - индекс не входит в диапазон списка
# list_ = [1, 2, 3]
# list_[4]


# TypeError - ошибка типов, когда тип объекта не подходит к операции
# str_ = 'youtube'
# num1 = 12
# str_ + num1

# int(12) # OK
# int(12.5) # OK
# print(int('103')) # OK
# print(int('dylbl')) # ValueError
# from math import sqrt
# print(sqrt(25)) # OK
# print(sqrt(-20)) # ValueError

# import wrong_module
# from math import wrong_module
# ошибки импорта 



# ошибка - проблема в синтаксисе кода. Например: нет скобки, двоеточия, отступа и т.д.

# SyntaxError - синтаксическая ошибка
# for i in range(1, 10)
#     print(i)


# IndentationError - ошибка отступа
# for i in range(1, 10):
# print(i)


# TabError - ошибка табуляции (смешивание пробелов и табуляций)
# for i in range(1,10):
#        print(i)


# print('Hello')
# print(10 / 0)
# print('World')


# try:
#     print('Hello')
#     print(10 / 0)
#     print('World')
# except:
#     print('что-то пошло не так')
# else:
#     print('try отработал без ошибок')
# finally:
#     print('я отработаю в любом случае')

# try:
#     попытка выполнить код, которая потенциально может вызвать исключение
# except:
#     обработка исключений - сработает, если в try есть исключение
# else:
#     выполняется, если try прошел без исключений
# finally:
#     выполняется в любом случае


# try:
#     print(c)
# except Exception as error:
#     print(error)

# print('другой участок кода')
# 10 + 10

# a = {'a': 10, 'b':20}
# try:
#     print(10 / 0)
#     print(a['d'])
# except KeyError:
#     print('Нет такого ключа')
# except ZeroDivisionError:
#     print('На ноль делить нельзя')

# print('другой участок кода')

# b = [1, 2, 3]
# try:
#     print[b[10]]
#     print(b.get(3))
# except (IndexError, AttributeError):
#     print('нет такого индекса или нет такого индекса')



# raise - оператор для генерации собственных исключений
# raise название_исключения(описание исключения)

# temperature = int(input())
# if temperature > 100:
#     raise Exception('температура не можетбыть выше 100 градусов')

# print('ещё какой-нибудь код')

# num1 = 10
# num2 = 0
# try:
#     num1 / num2
# except Exception:
#     print('На ноль делить нельзя')

# if num2 != 0:
#     num1 / num2
# else:
#     print("На ноль делить нельзя")


# try:
#     for i in range(1, 10)
#         print(i)
# except SyntaxError: # нельзя обработать
#     print('Неправильно написан код')
