import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        port="5434",
        user="postgres_task",
        password="student",
        database="student"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products;")
    results = cursor.fetchall()
    print("Результат запроса:")
    for row in results:
        print(row)
    cursor.close()
    conn.close() 
except Exception as e:
    print(f"Ошибка: {e}")