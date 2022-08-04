""" Кортеж(tuple)"""

# Кортеж - неизменяемая последовательность элементов.
# Ведет себя как список, но не изменяется.

# print(dir(tuple))

# my_tuple = (1, 2, 3, 4, 5) # tuple
# print(type(my_tuple))

# a = (2)
# print(type(a)) # int

# b = ('string',)
# print(type(b)) # tuple

# c = [1, 2, 3,], 'string', 3
# print(type(c)) # tuple

# d = 1,
# print(type(d)) # tuple


# tuple1 = (3, 3, 4, 5, 6, 3)
# print(tuple1.count(3)) # 3
# print(tuple1.index(4)) # 2


# num1 = 1
# num2 = 2
# num3, num4 = 4, 7
# print(num3, num4) 


# tuple2 =('str1', 'str2', 'str3' )
# print(*tuple2)
# print(tuple2[0], tuple2[1], tuple2[2])

# nums = (10, 5)
# print(pow(*nums))

# a, b, c, d, f = 1, 2, 3, 4
# print(a)
# print(b)
# print(c)


# a = (1, 2, 3, ['str1', 'str2'])
# # a[2] = 5 # Error
# a[3].append(4)
# print(a)


# new_tuple = (('name', 'Alina'), ('name', 'Marina'), ('name', 'Kayrat',), ('name', 'Mirbek'))

# for i in new_tuple:
#     print(i)

# for key, value in new_tuple:
#     print(key)
#     print(value)


# list_ = [1, 2, 3, 4, 5]
# for i in list_:
#     print(i)


# index = 0
# while index < len(list_): 
#     print(list_[index])
#     index += 1
    


# Написать программу, которая будет запрашивать количество денег, которое Вы хотите потратить.
# Если указанное число больше чем денег в кошельке - программа предупреждает об этом и останавливается.
# Иначе отнимает указанное число из кошелька и печатает количество оставшихся денег.

# while True:
#     money = 100000
#     buy = int(input())
#     if money > buy:
#         cash = money - buy
#         print(cash)
#     else:
#         print('Вам не хватает денег')
#         break

# len(последовательность) - возвращает количество элементов в последовательности
# max(последовательность)
# min(последовательность)
# sum(последовательность)


# numbers = (3, 6, 1, 4, 5)
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))


# tuple3 = (1, 2, 3)
# tuple3 = list(tuple3)
# print(tuple3)

# a = [1, 2, 3]
# b = (1, 2, 3)
# print(a.__sizeof__())
# print(b.__sizeof__())
