lines = open('9.in').read().splitlines()

part1 = 0
part2 = 0
for line in lines:
    arr = [int(x) for x in line.split()]
    G = [arr]
    while True:
        arr1 = []
        for i in range(len(arr) - 1):
            arr1.append(arr[i + 1] - arr[i])
        arr = arr1
        G.append(arr)
        s = set(arr)
        if len(s) == 1:
            break
    G.reverse()
    diff1 = 0
    diff2 = 0
    for arr in G:
        diff1 += arr[-1]
        diff2 = arr[0] - diff2
    part1 += diff1
    part2 += diff2
            
print(part1)
print(part2)
            
    
