# Read red tile coordinates
coords = []
with open("test9.txt", 'r') as file:
    for line in file:
        x, y = map(int, line.strip().split(','))
        coords.append((x, y))

rows = len(coords)

# Step 1: Generate all valid tiles (red + green along connecting paths)
valid_tiles = set()
for i in range(rows):
    x0, y0 = coords[i]
    x1, y1 = coords[(i + 1) % rows]  # wrap around

    if x0 == x1:  # vertical segment
        for y in range(min(y0, y1), max(y0, y1) + 1):
            valid_tiles.add((x0, y))
    elif y0 == y1:  # horizontal segment
        for x in range(min(x0, x1), max(x0, x1) + 1):
            valid_tiles.add((x, y0))
    else:
        raise ValueError("Non-axis-aligned segment found!")

# Step 2: Try all pairs of red tiles as opposite corners
max_area = 0
best_rect = None

for i in range(rows):
    for j in range(i + 1, rows):
        c1 = coords[i]
        c2 = coords[j]

        xmin, xmax = min(c1[0], c2[0]), max(c1[0], c2[0])
        ymin, ymax = min(c1[1], c2[1]), max(c1[1], c2[1])

        # Step 3: Generate the actual perimeter of rectangle along valid tiles
        # Only horizontal/vertical edges along valid_tiles
        edges = set()
        # bottom and top edges
        for x in range(xmin, xmax + 1):
            edges.add((x, ymin))
            edges.add((x, ymax))
        # left and right edges
        for y in range(ymin, ymax + 1):
            edges.add((xmin, y))
            edges.add((xmax, y))

        # Step 4: Check if all edge tiles exist in valid_tiles
        if edges.issubset(valid_tiles):
            area = (xmax - xmin + 1) * (ymax - ymin + 1)
            if area > max_area:
                max_area = area
                best_rect = (c1, c2)

print("Largest rectangle:", best_rect, "Area:", max_area)
