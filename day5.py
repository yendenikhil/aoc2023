sets = open('5.in', 'r').read().strip().split('\n\n')

G = []
seeds = []
for seed in sets[0].split(' ')[1:]:
    seeds.append(int(seed))

for s in sets[1:]:
    arr = []
    for line in s.split('\n')[1:]:
        arr.append([int(x) for x in line.split(' ')])
    G.append(arr)

def get_match(n, arr):
    ans = None
    for [d, s, r] in arr:
       if n >= s and n < s + r:
        ans = d + (n - s)
        break
    if ans == None:
        ans = n
    return ans

part1 = []
for seed in seeds:
    for arr in G:
        seed = get_match(seed, arr)
    part1.append(seed)
        
print(min(part1))

G2 = []
seeds2 = []
G.reverse()
for i in range(0, len(seeds), 2):
    seeds2.append((seeds[i], seeds[i] + seeds[i + 1]))
for arr in G:
    arr_adj = []
    for a in arr:
        arr_adj.append([a[1], a[0], a[2]])
    G2.append(arr_adj)

loc = 1
found = False
while True:
    curr = loc
    for arr in G2:
        curr = get_match(curr, arr)
    for (a, b) in seeds2:
        if curr >= a and curr < b:
            found = True
            break
    if found:
        break
    loc += 1

print(loc)
        
    



