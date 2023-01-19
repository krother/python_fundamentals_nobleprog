"""
The following program collects names in a list that occur at least 10000 times.

Unfortunately, the program contains four errors. Find and fix them.
"""
frequent = []

for line in open('babynames.csv'):
    columns = line.strip().split(',')
    name = colums[1]
    n = int(columns[3])
    if n >= 10000
        frequent.append(name)

print(frequent)
