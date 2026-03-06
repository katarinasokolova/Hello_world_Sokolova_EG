#!/bin/bash
for i in {1..20}; do
	if [ $((i % 2)) -eq 0 ]; then 
	continue
	elif [ $i -eq 15 ]; then
	break
	else
	echo "Нечетные числа: $i"
	fi
done
