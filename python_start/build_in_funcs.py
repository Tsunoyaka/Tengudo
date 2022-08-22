""" Встроенные функции """

# print()

# Приведение к определенному типу
# int()
# str()
# dict()
# list()
# set()
# tuple()
# bool()
# complex()
# float()


# pow()
# divmod()


# dir() - возвращает список атрибутов и методов переданного объекта
# type()
# id()
# a = 10
# print (isinstance(a, int))

# len()
# min()
# max()
# sum()



"""
map, filter, enumerate, zip, reduce

lambda
"""

# map(func, iterable) - принимает функцию и какой-то итерируемый объект. 
# Применяет переданную функцию к каждому элементу итерируемого объекта.


# def func1(num):
#     return num + 10

# nums = [1, 2, 3, 4, 5]

# res = list(map(func1, nums))
# res2 = [num + 10 for num in nums]
# print(res2)
# print(res)

# def func1(num, num2):
#     return num + num2

# nums = [1, 2, 3, 4, 5]
# nums2 = [1, 2, 3, 4, 5, 6]

# res = list(map(func1, nums, nums))

# words = ['apple', 'map', 'laptop']
# res = map(lambda word: word + '15', words)

# print(list(res))

# lambda param: тело функции - lambda - анонимная функция,
# которая живет только на момент ее выполнения



# filter(func, iterable) - принимает функцию(-> bool) и итер. объект
# Фильтрует по условию указанному в функции

# nums = [76, 89, 35, 65, 43, 85]
# def filter_num(num):
#     return num % 5 == 0

# res = list(filter(filter_num, nums))
# res2 = list(filter(lambda num: num % 5 == 0, nums))
# res3 = [num for num in nums if num % 5 == 0]


# print(res)
# print(res2)
# print(res3)


from ast import operator
from functools import reduce
import re
from typing import Iterable, Tuple

# reduce(func, iterable) - принимает функцию, итер. объект. 
# Сводит все элементы итер. объекта в одно значение

# nums = [10, 20, 30, 40]
# def func3(num1, num2):
#     return num1 + num2

# res = reduce(func3, nums)
# res2 = reduce(lambda num1, num2: num1 + num2, nums)
# res3 = [num + num for num in nums]
# print(res)
# print(res2)
# print(res3)
# print(sum(nums))

# nums = [10, 20, 30, 40]
# min_value = reduce(lambda x, y: x if x < y else y, nums)
# print(min_value)
# print(min(nums))


# enumerate(iterable) - принимает последовательность элементов, и нумерует каждый элемент последовательности

# a = 'word'
# res = enumerate(a)

# print(list(res))
# print(dict(res))

# b = ['h', 'e', 'l', 'l', 'o']
# res2 = enumerate(b, start=12)
# print(tuple(res2)) 
# for i in res2:
    # print(i)


# a = 'word'
# b = iter(a)
# while True:
#     try:
#         print(b.__next__())
#     except StopIteration:
#         break


# zip() - связывает элементы переданных последовательностей

# zipped_list = [1, 2, 3, 4, 5]

# print(zip(zipped_list))


""" all(), any() """

# all(iterable) - возвращает True, если ВСЕ элементы внутри последовательности являются True, иначе False

# list_ = [True, True, True]
# print(all(list_)) # True

# list_1 = [True, False, True]
# print(all(list_1))

# num = [9, 7, 1, 5, 6]
# print(all(num)) # True

# num2 = [9, 7, 0, 5, 6]
# print(all(num2)) # False

# 0
# False
# None
# ''
# []
# {}
# set()
# tuple()

# all('hello') # True
# all((1, 2, 3)) # True
# all(map(lambda x: x + 10, [1, 2, 3])) # True
# all(i for i in range(10)) # False


# def all(iterable):
#     for element in iterable:
#         if not element:
#             return False
#     return True


# any(iterable) - возвращает True, если ХОТЯ БЫ ОДИН один элемент в последовательности True, иначе False


# list_ = [True, True, True]
# print(any(list_)) # True

# list_2 = [False, True, False]
# print (any(list_2)) # False

# nums = ['', (), tuple(), set(), {}, False, None, 10]
# print(any(nums)) # True


# def any(iterable):
#     for element in iterable:
#         if element:
#             return True
#     return False


# password1 = 'mysuperpasswor'
# spec_symb = '@#?$'
# def check_password(password):
#     if not any(i.isupper() for i in password):
#         raise ValueError('Пароль должен содержать хотя бы 1 символ верхнего регистра')
#     if not any(i.isdigit() for i in password):
#         raise ValueError('Пароль должен содержать хотя бы 1 цифру')
#     if not any(i for i in password if i in spec_symb):
#         raise ValueError('Пароль должен содержать хотя бы спец. символ')
#     return password
# check_password(password1)


# callable(obj) - принимает объект и проверяет можно ли его вызвать

# def func(x):
#     return(x)


# print(callable(func)) # True

# a = 'string'
# print(callable(a)) # False
# a()

# def func2(x, y):
#     return x / y

# print(func2(10, 5))

# func3 = lambda x, y: x / y
# callable(func3) # True
# print(func3(20, 2))


# eval() - принимает какое-то утверждение и выполняет его 

# eval('print(10)')

# num1 = int(input(''))
# num2 = int(input(''))
# operator = input('')
# eval(f'print({num1}{operator}{num2})')

# res = map(lambda x: x * 2, range(1, 10))1
# for i in gen_func(10):
#     print(i)

# print(gen_func(19))