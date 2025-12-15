ranges = []
values = []
fresh = 0

with open("day5.txt") as file:
    section = 0  # 0 = ranges, 1 = values

    for line in file:
        line = line.strip()

        if line == "":
            section = 1
            continue

        if section == 0:
            start, end = map(int, line.split("-"))
            ranges.append((start, end))
        else:
            values.append(int(line))

ranges.sort()
print(ranges)

for i in values:
    for start, end in ranges:
        if i >= start and i <= end:
            fresh += 1
            #print(i)
            break

print(fresh)

