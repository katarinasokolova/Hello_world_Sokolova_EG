-- Таблица products
create table if not EXISTS products (
	id SERIAL primary key,
	name VARCHAR(100) not null,
	category VARCHAR(50)
	);

-- Таблица prices
create table if not EXISTS prices (
	id SERIAL primary key,
	product_id INTEGER references products(id),
	price numeric(10,2) not null,
	created_at TIMESTAMP default CURRENT_TIMESTAMP,
	foreign key (product_id) references products(id)
);

-- Таблица suppliers
create table if not EXISTS suppliers (
	id SERIAL primary key,
	name VARCHAR(100) not null,
	product_id INTEGER,
	foreign key (product_id) references products(id)
);
