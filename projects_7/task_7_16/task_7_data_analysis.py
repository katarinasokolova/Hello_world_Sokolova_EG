import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

DB_CONFIG = {
    "host": "localhost",
    "database": "student",
    "user": "postgres_task",
    "password": "student",
    "port": "5434"
}

try:
    conn = psycopg2.connect(**DB_CONFIG)
    print("Успешное подключение к базе данных")
except Exception as e:
    print(f"Ошибка подключения: {e}")
    exit()
# Запрос 1: Средняя цена по категориям (для сравнения)
# Мы берем последнюю (актуальную) цену для каждого товара, чтобы не искажать статистику историей цен
query_prices_by_category = """
SELECT p.category, latest_prices.price
FROM products p
JOIN (
    SELECT DISTINCT ON (product_id) product_id, price
    FROM prices
    ORDER BY product_id, created_at DESC
) latest_prices ON p.id = latest_prices.product_id;
"""
# Запрос 2: Количество поставщиков на один товар (анализ конкуренции/снабжения)
query_suppliers_per_product = """
SELECT p.name as product_name, COUNT(s.id) as supplier_count
FROM products p
LEFT JOIN suppliers s ON p.id = s.product_id
GROUP BY p.id, p.name
ORDER BY supplier_count DESC;
"""
# Загрузка данных в DataFrame
df_prices = pd.read_sql_query(query_prices_by_category, conn)
df_suppliers = pd.read_sql_query(query_suppliers_per_product, conn)

conn.close()
# Рассчитываем статистику для цен
mean_price = df_prices['price'].mean()
median_price = df_prices['price'].median()
std_price = df_prices['price'].std()

print(f"Общая статистика цен: Среднее={mean_price:.2f}, Медиана={median_price:.2f}")

# Настройка стиля графиков
sns.set_theme(style="whitegrid")
plt.figure(figsize=(20, 10))

# --- ГРАФИК 1: Boxplot (Ящик с усами) цен по категориям ---
plt.subplot(2, 2, 1)
sns.boxplot(x='category', y='price', data=df_prices, palette='Set2')
plt.title('Распределение цен по категориям товаров')
plt.xlabel('Категория')
plt.ylabel('Цена (руб)')
plt.xticks(rotation=45)

# Обоснование выбора:
# Boxplot идеально подходит для сравнения распределения данных между разными категориями
# и визуального выявления выбросов (аномалий).

# --- ГРАФИК 2: Гистограмма общего распределения цен ---
plt.subplot(2, 2, 2)
sns.histplot(df_prices['price'], bins=30, kde=True, color='skyblue')
# Добавляем линии среднего и медианы
plt.axvline(mean_price, color='red', linestyle='--', label=f'Среднее ({mean_price:.2f})')
plt.axvline(median_price, color='orange', linestyle='-', label=f'Медиана ({median_price:.2f})')
plt.title('Общее распределение цен на товары')
plt.xlabel('Цена')
plt.ylabel('Количество товаров')
plt.legend()

# Обоснование выбора:
# Гистограмма показывает форму распределения (нормальное, скошенное и т.д.).
# Линии среднего и медианы помогают понять смещение данных.

# Сохраняем и показываем графики
plt.tight_layout()
plt.savefig('analysis_report.png', dpi=300)
plt.show()

print("\n--- ОТЧЕТ ПО ЗАДАНИЮ ---")

print("\n1. График: Распределение цен по категориям (Boxplot)")
print("   - Выводы: Можно увидеть, в какой категории разброс цен больше (высокий ящик), а в какой цены стабильны.")
print("   - Аномалии: Точки выше верхнего 'уса' ящика являются ценовыми аномалиями (слишком дорогие товары для своей категории).")

print("\n2. График: Гистограмма цен")
print("   - Выводы: Если 'хвост' графика тянется вправо, значит, большинство товаров дешевые, но есть несколько очень дорогих.")
print(f"   - Статистика: Средняя цена {mean_price:.2f}, но если Медиана ({median_price:.2f}) значительно ниже, это подтверждает наличие дорогих выбросов.")