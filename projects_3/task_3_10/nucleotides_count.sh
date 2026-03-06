#!/bin/bash
printf "%-15s %-7s %-7s %-7s %-7s\n" "Файл" "A" "T" "G" "C"
for file in *.fasta; do
	if [ ! -s "$file" ]; then
		continue
	fi
	sequence=$(grep -v "^>" "$file" | tr -d '\n')
	count_a=$(echo "$sequence" | grep -o "A" | wc -1)
	count_t=$(echo "$sequence" | grep -o "T" | wc -1)
	count_g=$(echo "$sequence" | grep -o "G" | wc -1)
	count_c=$(echo "$sequence" | grep -o "C" | wc -1)
	printf "%-15s %-7s %-7s %-7s %-7s\n" "$file" "$count_a" "$count_t" "$count_g" "$count_c"
done
