# day 2 part 2 advent of code 2025
ranges = []
sum = 0

with open("day2.txt") as file:
    data = file.read().split(',')

    for section in data:
        if '-' in section:
            start, end = map(int, section.split('-'))
            ranges.append((start, end))
    
for start, end in ranges:
    for num in range(start, end + 1):
        s = str(num)
        seen = []

        # outer loop: finds possible multiples , 2-len(s)
        for i in range(1, len(s)//2 + 1):
            if len(s) % i == 0: # can the mult evenly divide

                #substring 101
                substring = s[0:i]

                valid = substring * (len(s) // i)

                if valid == s:
                    if num not in seen:
                        seen.append(num)
                        sum += num
                        print(num)

print("sum =", sum)
