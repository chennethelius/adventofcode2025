sum = 0
with open("day3.txt" , 'r') as file:
    for line in file:
        line = line.strip()

        dig1 = 0
        idx1 = 0

        # digit 1: loop through 0 - len(num) - 1
        for i in range(0, len(line)-1):
            digit = line[i]
            
            if int(digit) > dig1:
                dig1 = int(digit)
                idx1 = i
        
        dig2 = 0

        # digit 2: loop through line[idx1:]
        for i in range(idx1 + 1, len(line)):
            digit = line[i]
            
            if int(digit) > dig2:
                dig2 = int(digit)

        num = int(dig1*10 + dig2)
        sum += num
print(sum)