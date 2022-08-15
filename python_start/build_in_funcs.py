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


from functools import reduce
import re


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

# list1 = [1, 2, 3, 4, 5]

# print(list(zipped_list))