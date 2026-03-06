#!/bin/bash
echo "Введите ваш вес (в кг): "
read weight
echo "Введите ваш рост (в см): "
read height
bmi=$((weight * 10000 / (height * height)))
echo "Ваш ИМТ: $bmi"
