-- цена находится в диапазоне от 1000 до 50000 включительно
select *
from prices
where price between 1000 and 50000;

-- цена находится в диапазоне от 500 до 70000 и product_id меньше или равен 5
select *
from prices
where price between 500 and 70000 and product_id <= 5;

-- цена меньше 100 или цены находятся в диапазоне от 60000 до 70000
select *
from prices
where price < 100 or (price between 60000 and 70000);