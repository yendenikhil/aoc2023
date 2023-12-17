from collections import defaultdict, deque
G = []
for line in open('16.in').read().splitlines():
    arr = []
    for c in line:
        arr.append(c)
    G.append(arr)

rlen = len(G)
clen = len(G[0])
# define direction change first for \ as first list element and / for second list elem
dirchange = {
    (0, 1): [(1, 0), (-1, 0)],
    (0, -1): [(-1, 0), (1, 0)],
    (1, 0): [(0, 1), (0, -1)],
    (-1, 0): [(0, -1), (0, 1)]
}

ans = []
part1 = True
def draw(s):
    news = set()
    for (a, b, c, d) in s:
        news.add((a, b))
    for r in range(rlen):
        arr = []
        for c in range(clen):
            if (r, c) in news:
                arr.append('#')
            else:
                arr.append('.')
        # print(''.join(arr))
    # print(len(news))
    global part1
    if part1:
        print(len(news))
        part1 = False
    ans.append(len(news))

intial = []
for (a, b, c, d) in zip([* range(rlen)], [0] * rlen, [0] * rlen, [1] * rlen):
    intial.append((a, b, c, d))
for (a, b, c, d) in zip([* range(rlen)], [clen - 1] * rlen, [0] * rlen, [-1] * rlen):
    intial.append((a, b, c, d))
for (a, b, c, d) in zip([0] * clen, [* range(clen)], [1] * clen, [0] * clen):
    intial.append((a, b, c, d))
for (a, b, c, d) in zip([rlen - 1] * clen, [* range(clen)], [-1] * clen, [0] * clen):
    intial.append((a, b, c, d))
for e in intial:
    Q = deque([e])
    visited = set()
    while Q:
        r, c, dr, dc = Q.popleft()
    #    print(r, c, dr, dc)
        if 0 <= r < rlen and 0 <= c < clen:
            val = G[r][c]
            if (r, c, dr, dc) in visited:
                continue
            visited.add((r, c, dr, dc))
            if val == '.':
                Q.append((r + dr, c + dc, dr, dc))
            elif val == '|':
                if dr == 0:
                    Q.append((r + 1, c, 1, 0))
                    Q.append((r - 1, c, -1, 0))
                else:
                    Q.append((r + dr, c + dc, dr, dc))
            elif val == '-':
                if dc == 0:
                    Q.append((r, c + 1, 0, 1))
                    Q.append((r, c - 1, 0, -1))
                else:
                    Q.append((r + dr, c + dc, dr, dc))
            elif val == '\\':
                dr1, dc1 = dirchange[(dr, dc)][0]
                Q.append((r + dr1, c + dc1, dr1, dc1))
            elif val == '/':
                dr1, dc1 = dirchange[(dr, dc)][1]
                Q.append((r + dr1, c + dc1, dr1, dc1))

    draw(visited)

print(max(ans))
