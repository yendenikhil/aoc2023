lines = open('1.in').read().splitlines()

part1 = 0
part2 = 0
words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
for line in lines:
    first = None
    last = None
    for c in line:
        if c.isdigit():
            if first:
                last = c
            else:
                first = c
                last = c
    part1 += int(first+last)

print(part1)

# lines = open('1.2.in').read().splitlines()
for line in lines:
    first = None
    last = None
    for i in range(len(line)):
        if line[i].isdigit():
            if first:
                last = line[i]
            else:
                first = line[i]
                last = line[i]
        else:
            for w in words:
                if line[i:].startswith(w):
                    if first:
                        last = str(words.index(w))
                    else:
                        first = str(words.index(w))
                        last = str(words.index(w))
                    break
    part2 += int(first+last)

print(part2)
        
