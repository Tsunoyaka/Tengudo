""" Строки (string) """

# str ()

# Строки - неизменяемый, упорядоченный, индексируемый тип данных





from curses import raw, window


string = "Hello"

string2 = 'Hello'

doc_string = """ Обычно используется для написания документации к коду """ 

doc_string = ''' Обычно используется для написания документации в несколько строк ''' 

string3  = "Hello, i'm student "

string4 = 'Hello, i\'m teacher'


# str1 = 'Hello'
# str2 = 'World'
# print(str1 + str2)
# # Конкатенация - склеивание строк/сложение строк

# str3 = 'Quak'
# num1 = 3
# print (str3 * num1)

""" Функции и методы строк """
my_str = 'Hello world'

# print (len(my_str)) # - выводит длину строки
# print (my_str.split(separator)) # - делит по указанному делителю
# print(my_str.replace('l', 'b')) # hebbo worbd - замена подстроки

my_str.upper() # HELLO WORLD - перевод в верхний регистр
my_str.lower() # hello world - перевод в нижний регистр
my_str.title() # Hello World - переводтпервого символа каждого слова в верхний регистр
my_str.capitalize() # Hello world - перевод первого символа строки в верхний регистр
'ß'.casefold() # 'ß' - ss - эсцет - более агрессивный перевод в нижний регистр
my_str.count('l') # 3 - считает количество вхождений переданной подстроки

""" Индексы и срезы """

str7 = 'hello world'

# Индекс - порядковый номер символа в строке (начиная с 0)
# 'makers'
#  012345
# -054321
# print(str7[4])
# print(str7[10])
# print(str7[len(str7)-1])
# print(str7[-1])

str7 = 'hello world'

# print(str7[0:5])
# str7[start:stop]

# print(str7[4:]) # от старта до конца строки
# print(str7[:7]) # от начала до указанного индекса
# print(str7[0:-1:2]) # str7(start:stop:step)
# print(str7[::-1]) # отрицательный шаг начинает чтение строки с конца 

# str7 = 'hello world'
# print(str7.find('2')) # 1 - поиск индекса подстроки в строке
# print(str7.index('2')) 
# print('*'.join(['hello', 'world', 'bye'])) # соединяет переданный список строк по указанной строке

# str8 = 'my name is akbar'
# print(str8)
# print(str8.strip('')) # убирает указанный символ в строке с двух сторон, если не указан символ, по умолчанию - пробел
# # str8.lstrip() # - убирает пробелы слева
# # str8.rstrip() # - убирает пробелы справа

""" Методы проверки """
string = 'My test string 123'
# print(string.isdigit())
string.isalpha() # проверяет состоит ли текст лишь из буквенных символов
string.isalnum() # проверяет состоит ли текст лишь из цифр и буквенных символов
string.isspace() # проверяет состоит ли текст лишь
string.isupper() # проверяет состоит ли текст лишь вверхего регистра
string.islower() # проверяет состоит ли текст лишь нижнего регистра
string.endswith('123') # проверяет заканчивается ли текст на переданную подстроку
string.startswith('My') # проверяет начинается ли текст на переданную подстроку

num1 = 10
num2 = 20
num1 > num2  # False
num1 < num2  # True
num1 == num2 # False
num1 != num2 # True - неравество
num1 <= num2 # True
num1 >= num2 # False

# str1 = 'apple' 
# str2 = 'hello'
# print(str1 > str2)
# ord('a') # 97
# chr(97)  # 'a'
# ASCII

# a = 'abcde'
# b = 'abced'
# print(sorted(a))
# print(sorted(b))""


""" Форматирование/интерполяция строк """

# srat = 'Привет, Фархад! Приглашаю тебя на праздник'

# name = input()
# place = input()
# # %
# # str5 = 'Привет, %s! Приглашаю тебя на праздник' % name
# print(str5)
# str6 = 'Привет, {}! Приглашаю тебя на {}'.format(name, place)
# print(str6)

# str7 = f'Hello {name}! Welcome to {place}'
# print(str7)

# Форматирование строк - подстановка перменных в строку, создание динамической строки

# a = 'I\'m student'
# b = 'Идёт бычок качается,\n\tВздыхает на ходу'
# print(b)
# \n - newline
# \t - tabular 

# str8 = r'This is test string\n\t\n'
# print(str8)
# # raw - сырой
# #  \\ - сырой

# windows_path = 'Users\Documents\\new_folder'
# print(windows_path)

# string = 'Hello world'
# string2 = 'ell'
# print(string2 in string)

# dir(obj) - функция возвращает список методов доступных переданному объекту
# str1 = 'hello'
# print(dir(str1))