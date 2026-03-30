import math
N = int(input("Введите число N: "))
i = 1
max = -math.inf
while i <= N:
    number = float(input("Введите число: "))
    if number > max:
        max = number
    i = i + 1
print(f"Максимальное число: {max}")