-- количество поставщиков для каждого товара, сгрупированные по product_id
select product_id, COUNT(*)
from suppliers
group by product_id;