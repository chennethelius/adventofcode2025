coords = []
with open("day9.txt", 'r') as file:
    for line in file: 
        line = line.strip().split(',')
        coords.append((line))

rows = len(coords)
cols = len(coords[0])

coords.sort()

for c in coords:
    print(c)

areas = {}

for r in range(rows-1):
    for dr in range(r+1, rows):
        w = abs(int(coords[r][0]) - int(coords[dr][0])) + 1
        l = abs(int(coords[r][1]) - int(coords[dr][1])) + 1
        area = w*l
        areas[area] = [(coords[r]),(coords[dr])]

print(max(areas.keys()))
