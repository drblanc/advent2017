with open('advent5.txt', 'r') as myfile:
    jumplist = myfile.read()
    
jumps = [int(l) for l in jumplist.split()]
# jumps = [0, 3, 0, 1, -3]
last = len(jumps)

steps = 0
pos = 0
while pos >= 0 and pos < last:
    next = pos + jumps[pos]
    if jumps[pos] >= 3:
        jumps[pos] -= 1
    else:
        jumps[pos] += 1
    steps += 1
    pos = next
print(steps)