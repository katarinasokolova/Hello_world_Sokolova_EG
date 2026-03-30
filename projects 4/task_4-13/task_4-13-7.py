n = int(input("Введите количество элементов в массиве: "))
array = []
for i in range(0, n):
    array.insert(i, int(input("Введите элемент массива: ")))
sum = 0
i = 0
while i < n:
    sum = sum + array[i]
    i = i + 1
average = sum / n
print(f"Среднее арифметическое элементов массива: {average}")