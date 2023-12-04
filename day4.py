lines = open('4.in').read().splitlines()

part1 = 0
cards = []
for i in enumerate(lines):
    cards.append(1)

for i, line in enumerate(lines):
    card, nums = line.split(': ')
    left, right = nums.split('| ')
    arr = []
    for a in right.split():
        arr.append(int(a))
    count = 0
    for a in left.split():
        if int(a) in arr:
            count += 1
    if count > 0:
        part1 += pow(2, count - 1)
        for x in range(i + 1, i + 1 + count):
            cards[x] += cards[i] 

print(part1)

part2 = 0
for x in cards:
    part2 += x

print(part2)
