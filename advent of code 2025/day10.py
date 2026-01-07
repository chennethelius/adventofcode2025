matrix = []
with open("test10.txt", 'r') as file: 
    for line in file:
        line = line.strip()
        matrix.append(list(line.split()))

for row in matrix:
    print(row)

rows = len(matrix)
cols = len(matrix[0])

for row in range(rows):
    for col in range(cols):
        # read target = light config [.##.]
        target = matrix[row][0]

        # create off light config with len(target) [....]
        test = ['.' for i in range(len(target)-2)] # -2 because of [ and ]

        # grabs index of switches we need to turn on
        lightsOn = [num-1 for num in range(1,len(target)-1) if target[num] == "#"]

        # loop through buttons, avoid first and last index: button flipping logic
        if col > 0 and col < cols - 1:
            # part 1: button searching algo, do we search every combo of buttons possible? 
            # part 2: solution testing, how do we want to test the answer?

            # search by num of button in solution, 1 button soln, 2 button soln, ..., n button soln

            # turn all the lights on, then go back and turn off ones we don't need

            # hashmap solution: visited = {} key = num, value = count of nums

            pass

    print(row, target, lightsOn, test)

