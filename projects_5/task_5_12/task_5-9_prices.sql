-- количество записей для каждого товара
select product_id, COUNT(*)
from prices
group by product_id;

-- средняя цена товаров для каждого product_id
select product_id, AVG(price)
from prices
group by product_id;

-- минимальная цена товаров для каждого product_id
select product_id, MIN(price)
from prices
group by product_id;

-- максимальная цена товаров для каждого product_id
select product_id, MAX(price)
from prices
group by product_id;