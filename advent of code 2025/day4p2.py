matrix = []
total = 0

with open("day4.txt", "r") as f:
    for line in f:
        line = line.strip()        
        matrix.append(list(line)) 

def check(matrix):
    global total
    rows = len(matrix)
    cols = len(matrix[0])
    removable = 0

    newmatrix = nmatrix = [row[:] for row in matrix]

    for r in range(0, rows):
        for c in range(0, cols):
            if matrix[r][c] == '@':
                count = 0
                
                for x in range(-1,2):
                    for y in range(-1,2):
                        #bounds checker
                        if r+x < 0 or r+x >= rows:
                            continue
                        if c+y < 0 or c+y >= cols:
                            continue
                        if x == 0 and y == 0:
                            continue
                        
                        if matrix[r+x][c+y] == '@':
                            count += 1

                # check valid paper pos
                if count < 4:
                    removable += 1

                    #remove the paper
                    newmatrix[r][c] = 'x'
    
    total += removable

    if removable == 0:
        return newmatrix
    else:
        return check(newmatrix)

finalmatrix = check(matrix)

print(total)

