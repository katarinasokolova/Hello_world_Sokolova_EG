-- вывод 5 самих дорогих записей
select *
from prices
order by price
limit 5;

-- вывод 10 последних добавленных записей из таблицы prices, отсортированных по полю created_at
select *
from prices
order by created_at
limit 10;

-- вывод 10 самых дешёвых цен
select *
from prices
order by price asc
limit 10;

-- вывод пропуск первых 20 самых дорогих значений и отображение следующих
select *
from prices
order by price desc
limit 10 offset 20;