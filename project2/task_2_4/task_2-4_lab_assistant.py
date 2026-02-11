volume = int(input("Введите объём раствора (мл): "))
salt_mass = volume * 0.009
water_volume = volume
with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ\n")
    file.write("-"*23)
    file.write(f"\nОбщий объем: {volume} мл\nМасса соли: {salt_mass} г\nОбъем воды: {water_volume} мл")