from collections import defaultdict
order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
reorder = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'] 

games = defaultdict(list)
g2 = defaultdict(list)

for line in open('7.in', 'r').read().splitlines(): 
    cards, bid = line.split(' ')
    bid = int(bid)
    gcards = defaultdict(lambda: 0)
    gc2 = defaultdict(lambda: 0)
    j = 0

    for c in cards:
        gcards[c] += 1
    for c in cards:
        if c != 'J':
            gc2[c] += 1
        else:
            j += 1
    if len(gcards.keys()) == 1:
        games[6].append((cards, bid))
    elif len(gcards.keys()) == 2 and 4 in gcards.values():
        games[5].append((cards, bid))
    elif len(gcards.keys()) == 2 and 3 in gcards.values():
        games[4].append((cards, bid))
    elif len(gcards.keys()) == 3 and 3 in gcards.values():
        games[3].append((cards, bid))
    elif len(gcards.keys()) == 3:
        games[2].append((cards, bid))
    elif len(gcards.keys()) == 4:
        games[1].append((cards, bid))
    else:
        games[0].append((cards, bid))

    counts = sorted(gc2.values(), reverse=True)
    if not(counts):
        counts = [0]
    if counts[0] + j == 5:
        g2[6].append((cards, bid))
    elif counts[0] + j == 4:
        g2[5].append((cards, bid))
    elif counts[0] + j == 3 and counts[1] == 2:
        g2[4].append((cards, bid))
    elif counts[0] + j == 3:
        g2[3].append((cards, bid))
    elif counts[0] == 2 and (j or counts[1] == 2):
        g2[2].append((cards, bid))
    elif counts[0] == 2 or j:
        g2[1].append((cards, bid))
    else:
        g2[0].append((cards, bid))
        
        

for k in games.keys():
    games[k] = sorted(games[k], key=lambda s: ''.join([chr(65 + order.index(x)) for x in s[0]]), reverse=True)

for k in g2.keys():
    g2[k] = sorted(g2[k], key=lambda s: ''.join([chr(65 + reorder.index(x)) for x in s[0]]), reverse=True)
    

rank = 1
part1 = 0
for k in range(7):
    g = games[k]
    for (c, b) in g:
        part1 += rank * b
        rank += 1
print(part1)

rank = 1
part1 = 0
for k in range(7):
    g = g2[k]
    for (c, b) in g:
        part1 += rank * b
        rank += 1
print(part1)

