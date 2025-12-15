# day 1 part 2 advent of code 2025
dial = 50
count = 0

with open("day1.txt") as file:
    for line in file:
        rotation = int(line[1:])
        if line[0] == 'R':
            sign = 1 
        else:
            sign = -1

        start = dial
        end = start + rotation * sign

        if sign == 1:  # right
            count += (end // 100) - (start // 100)
        else:  # left
            count += ((start - 1) // 100) - ((end - 1) // 100)

        dial = end % 100

print(count)
