-- вывод всех товаров из таблицы
select *
from products;

-- вывод только названия и категории товара
select name, category
from products;

-- вывод всех уникальных категорий товаров
select distinct category
from products;

-- вывод товаров в алфавитном порядке
select *
from products
order by name asc;

-- вывод товаров в обратном алфавитном порядке
select *
from products
order by name desc;

-- вывод первых 10 строк
select *
from products
limit 10;

-- вывод 10 строк, начиная с 11 строки
select *
from products
limit 10 offset 10;

-- вывод 5 случайных товаров
select *
from products
order by random()
limit 5;

-- вывод всех категорий товаров в алфавитном порядке
select category
from products
order by category asc;

-- вывод всех категорий товаров сначала по категории, затем по названию
select *
from products
order by category asc, name asc;