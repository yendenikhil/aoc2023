from collections import defaultdict
from heapq import heapify, heappop, heappush
import math
G = []
for r, line in enumerate(open('17.in', 'r').read().splitlines()):
    arr = []
    for c, val in enumerate(line):
        arr.append(val)
    G.append(arr)
rlen = len(G)
clen = len(G[0])
dirs = [(0,1), (0, -1), (1, 0), (-1, 0)]

# heat, r, c, dr, dc, number of current straight
Q = [(0, 0, 0, 0, 0, 0)]
heapify(Q)
visited = set()
while Q:
    heat, r, c, dr, dc, num = heappop(Q)
    # print(heat, r, c, dr, dc, num)
    if r == rlen - 1 and c == clen - 1:
        print(heat)
        break
    if any((r, c, dr, dc, n) in visited for n in range(1, num + 1)):
        continue
    visited.add((r, c, dr, dc, num))
    for ndr, ndc in dirs:
        nr = r + ndr
        nc = c + ndc
        if ndr == dr and ndc == dc:
            nnum = num + 1
        else:
            nnum = 1
        if 0 <= nr < rlen and 0 <= nc < clen and nnum < 4:
            # print(nr, nc, nnum)
            if ndr == -dr and ndc == -dc:
                continue
            heappush(Q, (int(G[nr][nc]) + heat, nr, nc, ndr, ndc, nnum))
            

Q = [(0, 0, 0, 0, 1, 0), (0, 0, 0, 1, 0, 0)]
heapify(Q)
visited = set()
while Q:
    heat, r, c, dr, dc, num = heappop(Q)
    # print(heat, r, c, dr, dc, num)
    # print(f"p: ({r}, {c}) d: ({dr}, {dc}), {num}: {heat}")
    if r == rlen - 1 and c == clen - 1:
        if num > 3:
            print(heat)
            break
        else:
            continue
    if (r, c, dr, dc, num) in visited:
        continue
    visited.add((r, c, dr, dc, num))
    for ndr, ndc in dirs:
        nr = r + ndr
        nc = c + ndc
        if ndr == dr and ndc == dc:
            nnum = num + 1
        else:
            nnum = 1
        if 0 <= nr < rlen and 0 <= nc < clen and nnum < 11:
            if ndr == -dr and ndc == -dc:
                continue
            # print(">", nr, nc, ndr, ndc, nnum)
            if num < 4 and (ndr != dr or ndc != dc):
                continue
            # print(">>", nr, nc, ndr, ndc, nnum)
            heappush(Q, (int(G[nr][nc]) + heat, nr, nc, ndr, ndc, nnum))
