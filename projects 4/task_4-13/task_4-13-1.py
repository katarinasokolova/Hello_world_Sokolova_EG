a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
d = int(input("Введите четвёртое число: "))
min = a
if b < min:
    min = b
elif c < min:
    min = c
elif d < min:
    min = d
else:
    min = a
print(f"Минимальное число: {min}")