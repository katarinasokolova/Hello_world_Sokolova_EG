ph = float(input("Введите значение pH: "))
if ph < 7:
    print("Кислая среда")
elif ph > 7:
    print("Щелочная среда")
else:
    print("Нейтральная среда")