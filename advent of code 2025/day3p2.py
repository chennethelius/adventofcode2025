sum = 0
with open("day3.txt" , 'r') as file:
    for line in file:
        line = line.strip()

        #size of substring
        substrLen = len(line) - 12 + 1

        target = ""
        idx = 0
        length = 12

        remaining = 0

        while len(target) < length and (len(line) - idx) > (length - len(target)):
            # compute the size of the current window
            remaining_window = len(line) - idx - (length - len(target)) + 1
            window = line[idx : idx + remaining_window]

            # pick max in the current window
            tempMax = max(window)
            maxIdx = idx + window.index(tempMax)

            target += tempMax
            idx = maxIdx + 1

        # append the rest to get 12 total
        if len(target) < length:
            target += line[idx : idx + (length - len(target))]
        sum += int(target)

print(sum)