from collections import defaultdict

def f(mult = 1):
    ans = 0
    for line in open('12.in', 'r').read().splitlines():
        left, right = line.split()
        left = '?'.join([left] * mult)
        left, right = '.' + left + '.', eval(right)
        right = right * mult
        state = '.'
        for n in right:
            state += '#' * n
            state += '.'
        #print(left, state)
        Q = defaultdict(lambda: 0)
        Q[0] = 1
        for curr in left:
            NQ = defaultdict(lambda: 0)
            for k, v in Q.items():
                prev = state[k]
                if curr == '.':
                    if prev == '.':
                        NQ[k] += v
                    elif prev == '#' and k < len(state) - 1 and state[k + 1] == '.':
                        NQ[k + 1] += v
                elif curr == '?':
                    if prev == '#':
                        NQ[k + 1] += v
                    if prev == '.':
                        NQ[k] += v
                        if k < len(state) - 1:
                            NQ[k + 1] += v
                elif curr == '#':
                    if k < len(state) - 1 and state[k + 1] == '#':
                        NQ[k + 1] += v
            Q = NQ
            #print(curr, Q.items())
        #print(Q[len(state) - 2] + Q[len(state) - 1])
        ans += (Q[len(state) - 2] + Q[len(state) - 1])
                        
    print(ans)

f()
f(5)




