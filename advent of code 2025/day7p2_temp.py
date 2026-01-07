matrix = []
with open("day7.txt", 'r') as file:
    for line in file:
        line = line.strip("\n")
        if line:  # Only add non-empty lines
            matrix.append(list(line))

rows = len(matrix)
cols = len(matrix[0])

for r in range(rows-1):
    for c in range(cols):
        if (matrix[r][c] == 'S'):
            #set under to |
            matrix[r+1][c] = "|"

        #(split) when matrix[r][c] is ^: left and right to |, only split if above char is |
        if matrix[r][c] == '|' and matrix[r+1][c] == '^':
            matrix[r+1][c+1] = '|'
            matrix[r+1][c-1] = '|'

        #(extend) when below is not ^, if matrix[r][c] = |
        if matrix[r][c] == '|' and matrix[r+1][c] != '^':
            matrix[r+1][c] = '|'

for row in matrix:
    print(row)

# p2

count = 0

for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == "|":
            # check if this is a top endpoint (no | above)
            if r == 0 or matrix[r-1][c] != "|":
                if c == 0:
                    # At left edge - check if there's a ^ to the right
                    if c + 1 < cols and matrix[r][c+1] == "^":
                        count += 2  # Edge + split
                    else:
                        count += 1  # Just edge

                elif c == cols - 1:
                    # At right edge - check if there's a ^ to the left
                    if c - 1 >= 0 and matrix[r][c-1] == "^":
                        count += 2  # Edge + split
                    else:
                        count += 1  # Just edge

                else:
                    # Count based on ^ neighbors
                    left_is_caret = matrix[r][c-1] == "^"
                    right_is_caret = matrix[r][c+1] == "^"
                    
                    if left_is_caret and right_is_caret:
                        count += 2
                    elif left_is_caret or right_is_caret:
                        count += 1
                    else:
                        count += 1

print(count)