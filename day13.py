G = []
arr = []
for line in open('13.in', 'r').read().splitlines():
    if len(line) == 0:
        G.append(arr)
        arr = []
    else:
        arr.append(line)
G.append(arr)

ans = 0
for shape in G:
    rlen = len(shape)
    clen = len(shape[0])
    found = False
    for vsplit in range(1, clen):
        c1 = vsplit - 1
        c2 = vsplit
        mirror = True
        while c1 >= 0 and c2 < clen:
            for line in shape:
                if line[c1] != line[c2]:
                    mirror = False
                    break
            if not(mirror):
                break
            c1 -= 1
            c2 += 1
        if mirror:
            ans += vsplit
            break

    for hsplit in range(1, rlen):
        r1 = hsplit - 1
        r2 = hsplit
        mirror = True
        while r1 >= 0 and r2 < rlen:
            row1 = shape[r1]
            row2 = shape[r2]
            for c in range(0, clen):
                if row1[c] != row2[c]:
                    mirror = False
                    break
            if not(mirror):
                break
            r1 -= 1
            r2 += 1
        if mirror:
            ans += (100 * hsplit)
            break

print(ans)


ans = 0
for shape in G:
    rlen = len(shape)
    clen = len(shape[0])
    found = False
    for vsplit in range(1, clen):
        diff = 0
        c1 = vsplit - 1
        c2 = vsplit
        mirror = True
        while c1 >= 0 and c2 < clen:
            for line in shape:
                if line[c1] != line[c2]:
                    diff += 1
            if diff > 1:
                mirror = False
                break
            c1 -= 1
            c2 += 1
        if mirror and diff > 0:
            ans += vsplit
            break

    for hsplit in range(1, rlen):
        diff = 0
        r1 = hsplit - 1
        r2 = hsplit
        mirror = True
        while r1 >= 0 and r2 < rlen:
            row1 = shape[r1]
            row2 = shape[r2]
            for c in range(0, clen):
                if row1[c] != row2[c]:
                    diff += 1
            if diff > 1:
                mirror = False
                break
            r1 -= 1
            r2 += 1
        if mirror and diff > 0:
            ans += (100 * hsplit)
            break

print(ans)
