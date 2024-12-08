from collections import deque, defaultdict

steps = 64
steps2 = 26501365
G = []
for line in open('21.1.in', 'r').read().splitlines():
    if 'S' in line:
        start = (len(G), line.index('S'))
        start2 = (len(G), line.index('S'), 1)
    G.append([x for x in line])

# print(G)
rlen = len(G)
clen = len(G[0])
dirs = [x for x in zip([-1,0,1,0],[0,-1,0,1])]
Q = deque()
Q.append(start)
while steps > 0:
    steps = steps - 1
    NQ = set()
    #print(Q)
    while Q:
        (r, c) = Q.pop()
        #print(r, c)
        for (dr, dc) in dirs:
            nr = r + dr
            nc = c + dc
            #print(r, c, nr, nc)
            if nr >= 0 and nc >= 0 and nr < rlen and nc < clen and G[nr % rlen][nc % clen] != '#':
                NQ.add((nr, nc))
    Q = deque(NQ)
    #print(len(Q), Q)

print(len(Q))

    
Q = deque()
Q.append(start2)
steps2 = 10
while steps2 > 0:
    steps2 = steps2 - 1
    NQ = defaultdict(lambda: 0)
    #print(Q)
    while Q:
        (r, c, count) = Q.pop()
        #print(r, c)
        for (dr, dc) in dirs:
            nr = (r + dr) % rlen
            nc = (c + dc) % clen
            #print(r, c, nr, nc)
            if G[nr][nc] != '#':
                NQ[(nr, nc)] = NQ[(nr, nc)] + count
    Q = deque()
    for (r, c), count in NQ.items():
        Q.append((r, c, count))
    p1 = 0
    for (_,_,v) in Q:
        p1 += v
    print(p1, Q)


