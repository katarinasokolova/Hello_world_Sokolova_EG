-- группировка по категориям
select category, COUNT(*)
from products
group by category;

-- количество товаров, отсортированное по убыванию количества
select category, COUNT(*)
from products
group by category
order by count(*) desc;