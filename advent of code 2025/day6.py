matrix = []

with open("day6.txt", 'r') as file:
    for line in file:
        line = line.strip()
        row = line.split()
        matrix.append(row)

rows = len(matrix)
cols = len(matrix[0])

total = 0

for c in range(cols):
    calc = int(matrix[0][c])

    if matrix[rows-1][c] == '*':
        for r in range(1, rows-1): 
            calc *= int(matrix[r][c])
    else:  
        for r in range(1, rows-1):
            calc += int(matrix[r][c])

    total += calc

print(total)
