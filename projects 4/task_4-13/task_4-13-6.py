N = int(input("Введите число N: "))
sum = 0
i = 1
while i <= N:
    sum = sum + i**2
    i = i + 1
print(f"Сумма квадратов первых N чисел равна: {sum}")