lines = open('6.in').read().splitlines()
part1 = 1
for i, maxdist in enumerate(lines[1].split()):
    if i == 0:
        continue
    time = int(lines[0].split()[i])
    # print(f"i {i} time: {time}")
    count = 0
    for x in range(1, time):
        dist = (time - x) * x
        if dist > int(maxdist):
            count += 1
    part1 *= count

print(part1)

time = int(''.join(lines[0].split()[1:]))
maxdist = int(''.join(lines[1].split()[1:]))

mintime = 0
maxtime = 0
for x in range(1, time):
    dist = (time - x) * x
    if dist > maxdist:
        mintime = x
        break
for x in range(time, mintime, -1):
    dist = (time - x) * x
    if dist > maxdist:
        maxtime = x
        break

print(maxtime - mintime + 1)
