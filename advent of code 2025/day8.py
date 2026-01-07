coords = []
with open("day8.txt", "r") as file: 
    for line in file: 
        x, y, z = map(int, line.strip().split(","))
        coords.append([x, y, z])

def dist(x, y, z, x1, y1, z1) -> float:
    dx = (x - x1)**2
    dy = (y - y1)**2
    dz = (z - z1)**2

    return (dx + dy + dz) ** 0.5


rows = len(coords)
cols = len(coords[0])

distances = {}

# loop through and create key, value pairs of distance:(coords1), (coords2)
for i in range(rows-1):
    for j in range(i+1, rows):
        key = dist(coords[i][0], coords[i][1], coords[i][2], coords[j][0], coords[j][1], coords[j][2])
        distances[key] = ((coords[i][0], coords[i][1], coords[i][2]), (coords[j][0], coords[j][1], coords[j][2]))

distances = dict(sorted(distances.items()))

# list of circuits: [[C,D,X,Y,Z], 
#                    [A,B,P,L,O], 
#                    [E,F,R,T,U]] list of sets
circuits = []
count = 0

for j in distances.keys():

    if count >= 1000:
        break

    count += 1

    coord1 = distances[j][0]
    coord2 = distances[j][1]

    circ1 = None
    circ2 = None

    # loop through each coord in circuits
    for circuit in circuits:
        if coord1 in circuit:
            circ1 = circuit
        if coord2 in circuit:
            circ2 = circuit

    # two same circuit [A,B,C] C -> A: nothing happens --> check if both coordinates are in same row
    if circ1 and circ1 == circ2:
        continue

    # one circuit one single [A,B] -> C (B can't go back to A): append C to circuit list
    elif circ1 and circ2 is None:
        circ1.append(coord2)
    elif circ2 and circ1 is None:
        circ2.append(coord1)

    # both exist in a circuit, but not in the same circuit
    elif circ1 and circ2 and circ1 != circ2:
        circ1.extend(circ2)
        circuits.remove(circ2)

    # two single junctions A->B: create new circuit list
    else: 
        circuits.append([distances[j][0], distances[j][1]])


lengths = []

for c in circuits:
    lengths.append(len(c))

lengths = sorted(lengths)

print(lengths)