from collections import defaultdict
part1 = 0
def hash(s):
    score = 0
    for c in s:
        score += ord(c)
        score *= 17
        score %= 256
    return score

boxes = defaultdict(list)
for token in open('15.in').read().strip().split(','):
    part1 += hash(token)

    if token[-1] == '-':
        label = token[:-1]
        box = hash(label)
        for i, lens in enumerate(boxes[box]):
            l, p = lens
            if l == label:
                del boxes[box][i]
                break
    else:
        label, num = token.split('=')
        num = int(num)
        box = hash(label)
        replaced = False
        for i, lens in enumerate(boxes[box]):
            l, p = lens
            if l == label:
                replaced = True
                boxes[box][i] = (l, num)
                break
        if not(replaced):
            boxes[box].append((label, num))


print(part1)
part2 = 0
for k, v in boxes.items():
    for i, (l, p) in enumerate(v):
        part2 += (k + 1) * (i + 1) * p
print(part2)

            
        
    
