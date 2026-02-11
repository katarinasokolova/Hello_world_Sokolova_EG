capsules = int(input("Введите общее количество произведенных капсул: "))
packing_capacity = int(input("Введите количество капсул в одной упаковке: "))
full_packages = capsules // packing_capacity
remains = capsules - (full_packages * packing_capacity)
print("--- Отчёт фасовочного цеха ---")
print(f"Полных упаковок: {full_packages}\nОстаток капсул: {remains}")