# day 2 advent of code 2025
ranges = []
sum = 0

with open("day2.txt", 'r') as file:
    data = file.read().split(',')

    for section in data:
        if '-' in section:
            start, end = map(int, section.split('-'))
            ranges.append((start, end))
    
for start, end in ranges:
    for num in range(start, end + 1):
        s = str(num)
        mirror = len(s) // 2

        if s[:mirror] == s[mirror:]:
            sum += num

print(sum)


