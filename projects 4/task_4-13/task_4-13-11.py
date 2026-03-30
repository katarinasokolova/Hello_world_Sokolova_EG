n = int(input("Введите количество элементов в массиве: "))
array = []
for i in range(0, n):
    array.insert(i, int(input("Введите элемент массива: ")))
sum = 0
count = 0
i = 0
while i < n:
    sum = sum + array[i]
    count = count + 1
    i = i + 2
average = sum / count
print(f"Среднее арифметическое среди всех элементов с чётными индексами: {average}")