with open('02/input.txt') as moves:
    finalmove= 0
    finalmagnitude = 0
    for line in moves:
        move, magnitude = line.split()
        if move in ['up', 'down']:
            if move == 'down':
                finalmagnitude = finalmagnitude + int(magnitude)
            else:
                finalmagnitude = finalmagnitude - int(magnitude)
        if move == 'forward':
            finalmove = finalmove + int(magnitude)

print(finalmove * finalmagnitude)
# print(finalmagnitude)

with open('02/input.txt') as moves:
    aim = 0
    hposition = 0
    depth = 0
    for line in moves:
        move, magnitude = line.split()
        if move == 'down':
            aim = aim + int(magnitude)
        elif move == 'up':
            aim = aim - int(magnitude)
        elif move == 'forward':
            hposition = hposition + int(magnitude)
            depth = depth + (int(magnitude) * aim)

print(depth)
print(hposition)
        