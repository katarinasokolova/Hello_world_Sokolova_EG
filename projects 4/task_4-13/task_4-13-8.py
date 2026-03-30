n = int(input("Введите количество элементов в массиве: "))
array = []
for i in range(0, n):
    array.insert(i, int(input("Введите элемент массива: ")))
count = 0
i = 0
while i < n:
    if array[i] > 0:
        count = count + 1
    i = i + 1
print(f"Количество положительных чисел в массиве: {count}")