""" 
psql [dbname] [username] - вход в СУБД
\conninfo - информация о подключении
\с dbname [dbusername] - подключение к указанной бд
\l - просмотр доступных БД

Ключевые слова в SQL пишутся большими буквами, остальные строчными(не обязательно)
Конец команды обозначается символом ";"

CREATE DATABASE dbname; - создание БД
DROP DATABASE dbname; - удаление БД 

Создание таблиц
CREATE TABLE table_name(
    column_name data_type [constrain]
)
DROP TABLE table_name; - удаление таблицы

ALTER TABLE - изменение структуры таблицы
ALTER TABLE table_name ALTER COLUMN column_name SET/DROP NOT NULL/NULL/DATA TYPE/DEFOULT; -
- установка указанного ограничения
ALTER TABLE table_name RENAME TO new_table_name; - переименовка таблицы
ALTER TABLE table_name ADD COLUMN column_name data_type [constraint] - добавление столбца в таблицу
ALTER TABLE table_name ADD CONSTRAINT 'constraint name' CONSTRAINT (column_name) - установка ограничения на столбец


Типы данных
Числовые данные
1. Целые числа:
smallint - 2 байта, -32_768 до 32_767 (2^16)
int - 4 байта - -2_147_483_648 до 2_147_483_647 (2^32)
bigint - 8 байт - -9_223_372_036_854_775_808 до 9_223_372_036_854_775_807 (2^64)

2. Целые числа с автоувеличением:
smallserial - 1 до 32_767
serial - 1 до 2_147_483_647
bigserial - 1 до 9_223_372_036_854_775_807

3. Числа с плавающей точкой 
real - 4 байта, точность до 6 знаков после запятой
double precision - 8 байт, точность до 15 знаков после запятой
decimal - 131072 до запятой, до 16383 знаков после запятой
numeric - 131072 до запятой, до 16383 знаков после запятой

money - дробное число, с точностью до 2 знаков после запятой (200 > 200 сом)

Строчные типы данных
CHAR - строки с постоянной длиной (CHAR(10) -> 'hello_____')
VARCHAR - строки с максимальной длиной (VARCHAR(10) -> 'hello')
TEXT - строки с неограниченной длиной 

Boolean Type
t/f
True, False

Date/Time Types

timestamp (дата и время)
date (дата)
time (время)
interval (временной промежуток)

Enumerate Type - ограничение вариантов выбора, только для текстовых полей
CREATE TYPE gender AS ENUM('M', 'F')

Ограничения (constrains)
NULL, NOT NULL - ограничение, проверяющее можно ли в столбце указать пустое значение
UNIQUE - может ли значения в этом столбце повторяться
CHECK - проверка на условие (CHECK (age > 18))
DEFAULT - значение по умолчанию
PRIMARY KEY - определяет какой столбец будет идентификатором таблицы (NOT NULL + UNIQUE)
FOREIGN KEY - определяет какой столбец будет ссылкой на другую таблицу

Виды связей:
1. Один к одному

2. Один ко многим / Много к одному

3. Много ко многим 

"""