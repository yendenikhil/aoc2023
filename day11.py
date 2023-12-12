G = []
for line in open('11.in', 'r').read().splitlines():
    arr = []
    for c in line:
        arr.append(c)
    G.append(arr)

rows = []
cols = []
for i, line in enumerate(G):
    blank = True
    for c in line:
        if c == '#':
            blank = False
            break
    if blank:
        rows.append(i)

for i in range(len(G)):
    blank = True
    for j in range(len(G[0])):
        if G[j][i] == '#':
            blank = False
    if blank:
        cols.append(i)
        
S = []
for r, line in enumerate(G):
    for c, val in enumerate(line):
        if val == '#':
            S.append((r, c))

def solve(mult):
    ans = 0
    for i in range(len(S) - 1):
        for j in range(i + 1, len(S)):
            r1, c1 = S[i]
            r2, c2 = S[j]
            rc = 0
            cr = 0
            for rr in rows:
                if r1 < rr < r2 or r1 > rr > r2:
                    rc += 1
            for cc in cols:
                if c1 < cc < c2 or c1 > cc > c2:
                    cr += 1
            a = abs(r1 - r2)
            a += abs(c1 - c2)
            a += (rc * mult) 
            a += (cr * mult)
            ans += a 
    print(ans)

solve(1)
solve(999999)
