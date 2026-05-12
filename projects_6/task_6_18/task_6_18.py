import psycopg2
import pandas as pd
try:
    connection = psycopg2.connect(
        host="localhost", 
        port="5434",
        user="postgres_task",
        password="student",
        database="student" 
    )
    print("✓ Подключение установлено")
    query = """
        SELECT
            p.id AS price_id,
            pr.name AS product_name,
            pr.category,
            p.price,
            p.created_at
        FROM prices p
        JOIN products pr ON p.product_id = pr.id
        ORDER BY pr.category, pr.name
    """
    df = pd.read_sql(query, connection)
    print(df.head(10))
    print(df.info())
    print(f"\nВсего записей: {len(df)}")
    print(f"Уникальных товаров: {df['product_name'].nunique()}")
    print(f"Уникальных категорий: {df['category'].nunique()}")
    
    price_mean = df['price'].mean()
    price_median = df['price'].median()
    price_std = df['price'].std()
    price_min = df['price'].min()
    price_max = df['price'].max()
    print("\n === Метрики === ")
    print(f"Среднее значение: {price_mean:.2f} руб.\n")
    print(f"Медиана: {price_median:.2f} руб.\n")
    print(f"Стандартное отклонение: {price_std:.2f} руб.\n")
    print(f"Минимальная цена: {price_min} руб.\n")
    print(f"Максимальная цена: {price_max} руб.\n")

    q1 = df['price'].quantile(0.25)
    q2 = df['price'].quantile(0.50)
    q3 = df['price'].quantile(0.75)
    iqr = q3 - q1
    expensive_pr = df[df['price'] > q3][['product_name', 'category', 'price']].sort_values('price', ascending=False)
    print(f"Q1 (25%): {q1}")
    print(f"Q2 (50%): {q2}")
    print(f"Q3 (75%): {q3}")
    print(f"IQR (Q3 - Q1): {iqr}")
    print(expensive_pr.to_string(index=False))
    print(f"Количество продуктов, цена которых выше Q3: {len(expensive_pr)}")

    category_stats = df.groupby('category')['price'].agg(
        count = 'count',
        mean = 'mean',
        median = 'median',
        std = 'std'
    ).round(2)
    category_stats = category_stats.sort_values(by='mean', ascending=False)
    print("\n=== Сгруппированные данные ===")
    print(category_stats)

    price_range = df.groupby(['product_name', 'category'])['price'].agg(
        min_price = 'min',
        max_price = 'max'
    ).reset_index()
    price_range['price_diff'] = price_range['max_price'] - price_range['min_price']
    top_5 = price_range.sort_values(by='price_diff', ascending=False).head(5)
    print("\n=== Пять товаров с наибольшим разбросом цен === ")
    print(top_5[['product_name', 'category', 'min_price', 'max_price', 'price_diff']].to_string(index=False))

except Exception as error:
    print(f"Ошибка при подключении: {error}")