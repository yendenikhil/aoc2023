G = []
for line in open('14.in', 'r').read().splitlines():
    G.append([x for x in line])

deltas = [x for x in zip([1, 0, -1, 0], [0, 1, 0, -1])]
rlen = len(G)
clen = len(G[0])

def draw(G):
    for line in G:
        print(''.join(line))
    print()

def load(G):
    ans = 0
    for x in range(rlen):
        for v in G[x]:
            if v == 'O':
                ans += (rlen - x)
    print(ans)
        
def tos(G):
    ans = []
    for line in G:
        ans.append(''.join(line))
    return ''.join(ans)
def tog(string):
    G = []
    for line in string.split('\n'):
        G.append([x for x in line])
    return G
        

def tilt(G, tdir):
    dr, dc = deltas[tdir]
    if tdir < 2:
        for r in range(rlen):
            for c in range(clen):
                if G[r][c] == '.':
                    rr, cc = r + dr, c + dc
                    while 0 <= rr < rlen and 0 <= cc < clen:
                        if G[rr][cc] == 'O':
                            G[r][c] = 'O'
                            G[rr][cc] = '.'
                            break
                        elif G[rr][cc] == '#':
                            break
                        else:
                            rr, cc = rr + dr, cc + dc
    else:
        for r in reversed(range(rlen)):
            for c in reversed(range(clen)):
                if G[r][c] == '.':
                    rr, cc = r + dr, c + dc
                    while 0 <= rr < rlen and 0 <= cc < clen:
                        if G[rr][cc] == 'O':
                            G[r][c] = 'O'
                            G[rr][cc] = '.'
                            break
                        elif G[rr][cc] == '#':
                            break
                        else:
                            rr, cc = rr + dr, cc + dc

memo = {}
memo[tos(G)] = 0
tilt(G, 0)
load(G)
tilt(G, 1)
tilt(G, 2)
tilt(G, 3)
memo[tos(G)] = 1
maxcounter = 1000000000 
skip = 0

for counter in range(2, maxcounter + 1):
    tilt(G, 0)
    tilt(G, 1)
    tilt(G, 2)
    tilt(G, 3)
    string = tos(G)
    if string in memo.keys():
        loop = counter - memo[string]
        mult = (maxcounter - memo[string]) // loop
        skip = memo[string] + mult * loop + 1
        break
    memo[string] = counter
for counter in range(skip, maxcounter + 1):
    tilt(G, 0)
    tilt(G, 1)
    tilt(G, 2)
    tilt(G, 3)

load(G)
                    
