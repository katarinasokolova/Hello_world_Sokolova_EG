medium_name = input("Введите название питательной среды: ")
agar_concentration = input("Введите концентрацию агара (%): ")
temperature = input("Введите температуру стерилизации (°C): ")
with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"{medium_name}\n")
    file.write(f"-Концентрация агара: {agar_concentration}%\n")
    file.write(f"-Температура стерилизации: {temperature}°C\n")
print("Файл 'recipe.txt' успешно сформирован!")