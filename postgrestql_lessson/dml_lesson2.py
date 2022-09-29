"""
psql db_name < file_name - импорт
psql northwind < 11-fill_in_northwind.sql 



SELECT - выборка данных
SELECT * FROM table_name; - выборка всех полей
SELECT column_name FROM table_name - выборка указанных полей

Операторы сравнения:
> - больше
< - меньше
= - сравнения
>= - больше или равно
<= - меньше или равно
!= or <> - неравенство


WHERE - фильтрация данных
SELECT * FROM table_name WHERE condition;


AND - и 
OR - или
IN - в
BETWEEN - между
LIKE - подходит ли под шаблон (с учетом регистра)
ILIKE - без учета регистра
'%a%' - в слове есть буква 'a'
'a%' - слово начинает с 'a'
'%a' - слово заканчивается на 'a'
_ - количество андерскоров определяет количество символов

IS NULL - проверка на пустое значение
NOT - отрицания условия
LIMIT - установка количества выдаваемых  записей
ORDER BY - сортировка по полю 
GROUP BY - группировка по определенному столбцу
DESC - по убыванию, ASC - по возрастанию(по умолчанию)




UPDATE - обновление данных
UPDATE table_name SET column_name = value, column_name2 = value2 WHERE condition;
UPDATE products SET product_name = 'HelloWorld' WHERE product_name ILIKE 't%';

DELETE - удаление данных
DELETE FROM table_name - очистка всей таблицы
DELETE FROM table_name WHERE condition - очистка данных подходящих под условие
DELETE FROM products WHERE product_name ILIKE 'Hell%';


INSERT INTO - добавление данных 
INSERT INTO table_name (column_names) VALUES (values_for_columns); 


Функции PostgreSQL

Функции в PostgreSQL

Агрегационные функции:
COUNT() - функция для счета кол-ва вхождений
AVG() - поиск среднего значения
MAX() - поиск максимального значения
MIN() - поиск минимального значения
SUM() - поиск результата сложения всех значений

ROUND() - округляет значения с плавающей точкой
|| '' || - конкатенация
CASE WHEN - подстановка значений в зависимости от условий
SELECT column_name CASE WHEN condition THEN value1 ELSE value2 END FROM table_name




JOIN - связи между таблицами
FULL JOIN - соединяются все данные
LEFT JOIN - соединение из левой таблицы
RIGHT JOIN - соединение из правой таблицы
INNER JOIN - соединение только тех данных, которые имеют пересечение

SELECT * FROM person JOIN pets;
"""