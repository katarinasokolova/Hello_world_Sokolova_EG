operator_name = input("Введите имя оператора: ")
sensor_value = input("Введите текущее значение давления (Па): ")
with open("sensor_log.txt","w", encoding="utf-8") as file:
    file.write("ОПЕРАТОР\tЗНАЧЕНИЕ\n")
    file.write(f"{operator_name}\t{sensor_value}\n")
print("Данные успешно сохранены в sensor_log.txt")
