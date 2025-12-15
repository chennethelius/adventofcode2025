# day 1 advent of code 2025
dial = 50
count = 0

with open("day1.txt", 'r') as file:

    for line in file:

        # read r or l, get sign
        if line[0] == 'R':
            sign = 1
        else: 
            sign = -1

        dial += sign * int(line[1:])
        # wrap around
        dial %= 100

        if dial == 0:
            count += 1

print(count)