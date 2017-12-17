def fastjudge():
    A, B = 783, 325

    count = 0
    for _ in range(5000000):
        Acond = True
        while Acond:
            A = (A * 16807) % 2147483647
            Acond = A & 3
        Bcond = True
        while Bcond:
            B = (B * 48271) % 2147483647
            Bcond = B & 7
        if (A&0xffff) == (B&0xffff):
            count += 1
    print(count)

fastjudge()

