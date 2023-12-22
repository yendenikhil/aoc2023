from collections import deque
modules = {}
flipflop = {}
inv = {}
for line in open('20.in', 'r').read().splitlines():
    label, targetsraw = line.split(' -> ')
    targets = targetsraw.split(', ')
    if label == 'broadcaster':
        modules[label] = targets
    elif label[0] == '%':
        modules[label[1:]] = targets
        flipflop[label[1:]] = 'off'
    elif label[0] == '&':
        modules[label[1:]] = targets
        inv[label[1:]] = []
    else:
        print('wtf')

for key in inv:
    for label, targets in modules.items():
        for target in targets:
            if key == target:
                inv[key].append(('low', label))
def update_inv(pulse, target):
    for key, targets in inv.items():
        change = False
        for curr_pulse, curr_target in targets:
            if curr_target == target and curr_pulse != pulse:
                change = True
                inv[key].remove((curr_pulse, curr_target))
        if change:
            inv[key].append((pulse, target))
    #print(inv)
            
        

low = 0
high = 0
kh = 0
lz = 0
tg = 0
hn = 0
done = False

for c in range(1000000):
    Q = deque()
    Q.append(('low', 'broadcaster'))
    while Q:
        pulse, label = Q.popleft()
        # print(pulse, label)
        if pulse == 'low':
            low += 1
        else:
            high += 1
        if label == 'broadcaster':
            for target in modules[label]:
                Q.append((pulse, target))
        else:
            if label in flipflop:
                if pulse == 'high':
                    continue
                else:
                    if flipflop[label] == 'high':
                        pulse = 'low'
                    else:
                        pulse = 'high'
                    flipflop[label] = pulse
                    for target in modules[label]:
                        Q.append((pulse, target))

            elif label in inv:
                if all('high' == p for p, t in inv[label]):
                    pulse = 'low'
                else:
                    pulse = 'high'
                if label == 'kh' and pulse == 'high':
                    kh = c + 1
                if label == 'lz' and pulse == 'high':
                    lz = c + 1
                if label == 'tg' and pulse == 'high':
                    tg = c + 1
                if label == 'hn' and pulse == 'high':
                    hn = c + 1
                if kh > 0 and lz > 0 and tg > 0 and hn > 0:
                    done = True
                    break
                for target in modules[label]:
                    Q.append((pulse, target))
        update_inv(pulse, label)
    # print('---------')
    if done:
        break
    if c == 999:
        print(low * high)

print(kh * lz * tg * hn)


