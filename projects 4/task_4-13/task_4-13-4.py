N = int(input("Введите количество чисел: "))
sum = 0
for i in range(1, N + 1):
    sum = sum + i
    i = i + 1
print(f"Сумма первых {N} натуральных чисел: {sum}")