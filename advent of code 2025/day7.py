matrix = []
with open("day7.txt", 'r') as file:
    for line in file:
        line = line.strip("\n")
        matrix.append(list(line))

rows = len(matrix)
cols = len(matrix[0])

# S -> matrix[0][cols//2 + 1]
count = 0

for r in range(rows-1):
    for c in range(cols):
        if (matrix[r][c] == 'S'):
            #set under to |
            matrix[r+1][c] = "|"

        #(split) when matrix[r][c] is ^: left and right to |, only split if above char is |
        if matrix[r][c] == '|' and matrix[r+1][c] == '^':
            matrix[r+1][c+1] = '|'
            matrix[r+1][c-1] = '|'
            count += 1

        #(extend) when below is not ^, if matrix[r][c] = |
        if matrix[r][c] == '|' and matrix[r+1][c] != '^':
            matrix[r+1][c] = '|'

for row in matrix:
    print(row)
print(count)