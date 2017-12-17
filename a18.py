def spinlock0(stepsize = 394):
    curr = 0
    len = 1
    after = 0
    buffer = [0]
    for i in range(1,50000000+1):
        curr = (curr + stepsize) % len
        if curr == 0:
            after = i
        len += 1
        curr += 1
    return after

def spinlock(stepsize = 394):
    curr = 0
    len = 1
    buffer = [0]
    for i in range(1,50000000):
        curr = (curr + stepsize) % len
        buffer.insert(curr+1, i)
        len += 1
        curr += 1
    return buffer[buffer.index(0)+1]

print(spinlock0())

