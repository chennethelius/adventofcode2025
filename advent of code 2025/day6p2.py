matrix = []

with open("day6.txt", 'r') as file:
    for line in file:
        line = line.strip("\n")
        row = []
        for char in line:
            row += char
        matrix.append(row)

rows = len(matrix)
cols = len(matrix[0])
print(rows)

for row in matrix:
    print(row)

# distance in matrix[rows-1][0], last row from each operator to operator
distances = []
dist = 0
for c in range(cols):
    if matrix[rows-1][c] == '*' or matrix[rows-1][c] == '+' or c == cols-1:
        if dist != 0:
            distances.append(dist)
        dist = 0
    dist += 1

distances[-1] += 1

print(distances)

total = 0
start_calc = 0

for dist in distances:
    end_calc = start_calc + dist

    mult = 1
    add = 0
    #matrix read one rol at a time, row by row to read vertically
    for c in range(start_calc, end_calc):

        num = ''
        for r in range(rows-1):
            if matrix[r][c] == ' ':
                continue
            num += matrix[r][c]
        print("num is ", num)

        if matrix[rows-1][start_calc] == "*" and num != '':
            mult *= int(num)
        elif matrix[rows-1][start_calc] == "+" and num != '':
            add += int(num)
    
    print("total is ", max(mult, add))
    if mult == 1:
        total += add
    else:
        total += mult

    print("end block")

    start_calc = end_calc
print(total)