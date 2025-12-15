ranges = []
fresh = set()

with open("day5.txt") as file:

    for line in file:
        line = line.strip()
        if line == "":
            break
        start, end = map(int, line.split("-"))
        ranges.append([start, end])

ranges.sort()

#remove overlap
for i in range(0, len(ranges)-1):
    #check upper bound with next lower bound
    if ranges[i][1] >= ranges[i+1][0]:
        if ranges[i][1] <= ranges[i+1][1]:
            ranges[i][1] = ranges[i+1][1]
            ranges[i+1][0] = ranges[i+1][1]
        else:
            ranges[i+1][0] = ranges[i][1] 
            ranges[i+1][1] = ranges[i][1] 

difference = 0

#calculate differences
for i in range(0, len(ranges)-1):
    diff = ranges[i][1] - ranges[i][0] + 1
    if ranges[i][0] == ranges[i-1][1]:
        diff -= 1
    difference += diff
    #print(diff, ranges[i][1], ranges[i][0])

print(difference)