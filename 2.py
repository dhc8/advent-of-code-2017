import csv


with open("2.tsv") as tsv:
    checksum = 0
    div_sum = 0
    tsv = csv.reader(tsv, delimiter="\t")
    for row in tsv:
        vals = sorted([int(i) for i in row])
        # checksum += max(vals) - min(vals)
        for i in range(len(vals)):
            val_index = len(vals) - i - 1
            val = vals[val_index]
            for factor in vals[0:val_index]:
                if val % factor == 0:
                    div_sum += (val / factor)
                    break
# print(checksum)
print(div_sum)