"""
Identify frequent names
"""

frequent = []
path = '/home/kristian/projects/python_fundamentals_nobleprog/data_structures/'
total = 0

for line in open(path + 'bigbang_names.csv'):
    columns = line.strip().split(',')
    name = columns[0]
    n = int(columns[2])
    if n >= 1000:
        frequent.append(name)
    total += n

print(frequent)
print(total)
