lines = (open('3.in', 'r')).read().splitlines()

G = []
coords = [-1, 0, 1]
for r, line in enumerate(lines):
    d = ''
    iss = False
    nn = set()
    for c, val in enumerate(line):
        if val.isdigit() and not(iss):
            iss = True
            d = val
            nn = set()
            for i in coords:
                for j in coords:
                    nn.add((r + i, c + j))
        elif val.isdigit() and iss:
            d += val
            for i in coords:
                for j in coords:
                    nn.add((r + i, c + j))
        if iss and (not(val.isdigit()) or c == len(line) - 1):
            iss = False
            nn1 = set()
            for (a, b) in nn:
                if a >= 0 and b >= 0 and a < len(lines)  and b < len(line):
                    nn1.add((a, b))
            G.append((int(d), nn1))

part1 = 0
for arr in G:
    for (a, b) in arr[1]:
        if not(lines[a][b].isdigit()) and lines[a][b] != '.':
            # print(arr[0], a, b)
            part1 += arr[0]
            break

print(part1)

def get_nums(r, c):
    nums = []
    for arr in G:
        if (r, c) in arr[1]:
            nums.append(arr[0])
    return nums

GG = {}
for r, line in enumerate(lines):
    for c, val in enumerate(line):
        if val == '*':
            GG[(r, c)] =  get_nums(r, c)

part2 = 0
for k, val in GG.items():
    if len(val) == 2:
        part2 += (val[0] * val[1])
print(part2)
