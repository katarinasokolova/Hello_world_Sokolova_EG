files = ["seq1", "seq2", "seq3", "seq4"]
sample_date = "19.02.2025"
for name in files:
    new_name = sample_date + "_" + name + ".fasta"
    print(f"{new_name}")