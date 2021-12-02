
with open('01/input.txt') as scans:
    global prev
    prev = 10000000
    count = 0
    for line in scans:
        if int(line) > prev:
            count=count+1
        prev = int(line)
    print(count)

with open('01/input.txt') as scans2:
    global prev1, prev2, prev3
    prev1, prev2, prev3 = 0, 0, 0
    count = 0
    for line in scans2:
        if prev1==0:
            prev1=int(line)
            continue
        if prev2==0:
            prev2=int(line)
            continue
        if prev3==0:
            prev3=int(line)
            continue
        if any(elem is not 0 for elem in [prev1, prev2, prev3]):
            if int(line)+prev3+prev2 > prev1+prev2+prev3:
                count=count+1
            prev1 = prev2
            prev2 = prev3
            prev3 = int(line)
    print(count)
