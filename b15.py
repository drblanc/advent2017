from itertools import izip

def generator(factor = 16807, start = 65, mult = 4):
    val = start
    while True:
        val = (val * factor) % 2147483647
        if val % mult == 0:
            yield (val & 0xffff)

def judge():
    print("starting A")
    genA = generator(factor = 16807, start = 783, mult = 4)
    print("starting B")
    genB = generator(factor = 48271, start = 325, mult = 8)
    print("going")
    C = izip(genA, genB)

    count = 0
    for _ in range(5000000):
        a,b = C.next()
        if a == b:
            count += 1
    print(count)
    
judge()
