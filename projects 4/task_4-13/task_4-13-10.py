n = int(input("Введите количество элементов в массиве: "))
array = []
for i in range(0, n):
    array.insert(i, int(input("Введите элемент массива: ")))
sum = 0
i = 1
while i < n:
    sum = sum + array[i]
    i = i + 2
print(f"Сумма всех элементов с нечётными индексами: {sum}")