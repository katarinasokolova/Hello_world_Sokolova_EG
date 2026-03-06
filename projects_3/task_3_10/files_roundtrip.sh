#!/bin/bash
for i in {1..10}; do
	touch "test{$i}.txt"
	echo "Создан файл: test${i}.txt"
done

echo "Файлы созданы"
ls test*.txt

i=10
while [ $i -ge 1 ]; do
	rm "test${i}.txt"
	echo "Удалён файл test${i}.txt"
	((i--))
done
