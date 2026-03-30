N = int(input("Введите число: "))
a = 1
b = 1
while a <= N:
    b = b*a
    a = a + 1
print(f"Факториал числа {N} равен {b}")