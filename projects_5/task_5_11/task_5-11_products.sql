-- вывод всех товаров из раздела "электроника"
select *
from products
where category = 'Электроника';

-- вывод товаров из категории "одежда" с названием "женские"
select *
from products
where category = 'Одежда' and name like '%женские%';

-- товары, которые относятся к категории "продукты" или "книги"
select *
from products
where category = 'Продукты' or category = 'Книги';

-- товары, которые не относятся к категории "бытовая техника"
select *
from products
where not category = 'Бытовая техника';

-- товары, которые относятся к одной из категорий: "электроника", "одежда", "книги"
select *
from products
where category in ('Электроника', 'Одежда', 'Книги');

-- товары, в категории "электроника" с названием "Samsing" или не относящиеся к бытовой технике
select *
from products
where (category = 'Электроника' and name like '%Samsung%') or category = 'Бытовая техника';

-- товары, относящиеся к одной из категорий и их id находится в диапазоне, и название не Samsung
-- или относятся к категории "Книги"
select *
from products
where (category in ('Электроника', 'Одежда', 'Бытовая техника') and id between 1 and 15 and name not like '%Samsung%') or category = 'Книги';