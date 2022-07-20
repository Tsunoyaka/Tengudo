""" Строки (string) """

# str ()

# Строки - неизменяемый, упорядоченный, индексируемый тип данных



from symtable import Symbol


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

str7 = 'hello world'
# print(str7.find('2')) # 1 - поиск индекса подстроки в строке
# print(str7.index('2')) 
# print('*'.join(['hello', 'world', 'bye'])) # соединяет переданный список строк по указанной строке

str8 = 'my name is akbar'
print(str8)
print(str8.strip('')) # убирает указанный символ в строке с двух сторон, если не указан символgittt, по умолчанию - пробел
# str8.lstrip() # - убирает пробелы слева
# str8.rstrip() # - убирает пробелы справа