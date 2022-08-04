# привет - hello

""" Словари(dict) """
# Словарь - изменяемый, итерируемый. Состоят из пар: ключ: значение. Ключи могут быть только неизменяемые типы данных(
# tuple, str, int, None, bool), а значениям любые. Ключи должны быть уникальными.
# dict_ = {}
# password = {'name': 'Айбек', 'last_name': 'Абдулаев', 'age': 23, 'gender': 'M', 'birthday': '13.03.1997'}

# print(password['name']) # Айбек
# print(password['age'])  # 23

# dict2 = dict(name='Барсбек', last_name='Михаилов', age=19)
# print(dict2['age']) # 13

# dict3 = dict.fromkeys(['a', 'b'], 25)
# print(dict3) # {'a': 25, 'b': 25}

# dict4 = dict.fromkeys(['a', 'b'])
# print(dict3) # {'a': None, 'b': None}

# dict5 = dict([('name', 'John'), ('list_name', 'Watson')])
# print(dict5)


""" Методы словарей """

password = {'name': 'Айбек', 'last_name': 'Абдулаев', 'age': 23, 'gender': 'M', 'birthday': '13.03.1997'}

# password['name'] # Айбек
# print(password('id')) # KeyError

# print(password.get('name')) # Айбек
# print(password.get('id')) # None

# dict.get(key, None) - отдает значение указанного ключа, 
# если нет - отдает второе указанное значение ( по умолчанию  None)

# print(password.get('id', 'Нет такого ключа!')) # Нет такого ключа!


# password.setdefault(key, None) - отдаёт значение указанного ключа,
# если его нет - создаёт его со значением defoult( по умолчанию - None )

# print(password.setdefault('age')) # 23
# print(password.setdefault('id')) # None
# print(password.setdefault('id', 67690))
# print(password)


# password.update({key: value}) - принимает в себя другой словарь и обновляет исходний за счет него 

# dict8 = {'name': 'Майрам', 'age': 27, 'name': 'Азамат', 'id': 67869}
# password.update(dict8)
# print(password)
# print(dict8)


# a = {'a': 10, 'b': 20}
# a['c'] = 30
# a['a'] = 40
# print(a) # {'a': 40, 'b': 20, 'c': 30}


dict10 = {'name': 'Алия', 'last_name': 'Эрмекова', 'age': 21 }

# deleted_el = dict10.pop('nam','Нет такого ключа!')
# print(deleted_el)
# print(dict10)


# dict10.popitem()
# print(deleted_el)
# print(dict10) 

# dict10.clear()
# print(dict10) # {}

# del dict10['age']
# print(dict10)


iter_dict = {'a':10, 'b': 20, 'c': 30, 'd': 40}
# for i in iter_dict:
#     print(i) # keys

# for i in iter_dict:
#     print(iter_dict[i]) # values


""" keys(), values(), items() """

k = iter_dict.keys()
# print(k)
# for key in k:
#     print(key)

v = iter_dict.values()
# print(v)
# for values in v:
#     print(values)

i = iter_dict.items()
# print(i)
# for key, value in i:
#     print(f'ключи {key}, значения {value}')

# contacts = {
#     'names': {
#         "Aidar": 890787890,
#         'Baatai': 56747869,
#         'Igor': 56838458
#     }
# }
# print(contacts['names']['Igor'])

# names = contacts['names']
# print(names['Igor'])

# copy() - копирукет словарь
# contacts_copy = contacts.copy()
# print(contacts_copy)