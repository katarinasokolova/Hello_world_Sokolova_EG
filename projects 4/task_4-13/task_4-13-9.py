n = int(input("Введите количество элементов в массиве: "))
array = []
for i in range(0, n):
    array.insert(i, int(input("Введите элемент массива: ")))
sum = 0
i = 0
while i < n:
    if array[i] % 2 == 1:
        sum = sum + array[i]
    i = i + 1
print(f"Сумма всех нечётных элементов массива: {sum}")