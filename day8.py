import math
lines = open('8.in').read().splitlines()

instr = lines[0]
G = {}
for line in lines[2:]:
    fr, to = line.split(' = (')
    left, right = to[:-1].split(', ')
    G[fr] = (left, right)

def calc_steps(curr):
    s = 0
    while True:
        if curr[-1] == 'Z':
            # print(s)
            break
        to = instr[s % len(instr)]
        if to == 'L':
            curr = G[curr][0]
        else:
            curr = G[curr][1]
        s += 1
    return s


print(calc_steps('AAA'))
steps = set()
for curr in G.keys():
    if curr[-1] != 'A':
        continue
    steps.add(calc_steps(curr))

lcm = 1
for x in steps:
    lcm = abs(lcm*x) // math.gcd(lcm, x)

print(lcm)
