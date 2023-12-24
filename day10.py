from collections import deque

G = []
for line in open('10.in', 'r').read().splitlines():
    if 'S' in line:
        start = (len(G), line.index('S'))
    G.append([x for x in line])

# print(G)
rlen = len(G)
clen = len(G[0])

dirs = [ (-1, 0), (0, 1), (1, 0), (0, -1)]
shapes = {
    'S': ['F7|', 'J7-', 'LJ|', 'LF-'],
    '|': ['SF7|', '', 'SLJ|', ''],
    '-': ['', 'SJ7-', '', 'SLF-'],
    'L': ['SF7|', 'SJ7-', '', ''],
    'J': ['SF7|', '', '', 'SLF-'],
    '7': ['', '', 'SLJ|', 'SLF-'],
    'F': ['', 'SJ7-', 'SLJ|', ''] }

Q = deque([(*start, 0, set())])
part1 = 0
while Q:
    if part1 > 0:
        break
    r, c, steps, visited = Q.popleft()
    visited.add((r, c))
    poss = shapes[G[r][c]]
    for i in range(4):
        if part1 > 0:
            break
        dr, dc = dirs[i]
        nr, nc = r + dr, c + dc
        if 0 <= nr < rlen and 0 <= nc < clen and G[nr][nc] in poss[i]:
            if G[nr][nc] == 'S' and steps > 1:
                vv = visited
                part1 = (steps + 1) // 2
                break
            if not((nr, nc) in visited):
                Q.appendleft((nr, nc, steps + 1, set(visited)))
print(part1)

part2 = 0
for r in range(rlen):
    for c in range(clen):
        if (r, c) in vv:
            continue
        x, y, crosses = r, c, 0
        while x < rlen and y < clen:
            if (x, y) in vv and not(G[x][y] in 'L7'):
                crosses += 1
            x += 1
            y += 1
        if crosses % 2 == 1:
            part2 += 1

print(part2)
        
            
        
    


