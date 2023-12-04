lines = open('2.in').read().splitlines()

colors = ['red', 'green', 'blue']
part1 = 0
part2 = 0
for line in lines:
    gameline, setsline = line.split(': ')
    game = int(gameline.split(' ')[1])
    failed = False
    r = 0
    g = 0
    b = 0
    for ss in setsline.split('; '):
        s = [0, 0, 0]
        for e in ss.split(', '):
            v, c = e.split(' ')
            s[colors.index(c)] = int(v)
        r = max(r, s[0])
        g = max(g, s[1])
        b = max(b, s[2])
        if s[0] > 12 or s[1] > 13 or s[2] > 14:
            failed = True
    part2 += (r * g * b)
    if not(failed):
        part1 += game

print(part1)
print(part2)


