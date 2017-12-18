inputstring = """set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 826
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19"""

from collections import defaultdict

def sndchip(st):
    regs = defaultdict(int)
    queue = [[],[]]
    prog = []
    for l in st.splitlines():
        par = l.split(' ')
        prog.append((par[0],par[1:]))

    def val(cpu,s):
        if s in 'abcdefghijklmnopqrstuvwxyz':
            return regs[(cpu,s)]
        else:
            return int(s)
    pc = [0, 0]
    regs[(1,'p')] = 1
    waiting = [False, False]
    freq = 0
    cpu = 0
    sent = 0
    while True:
        if waiting == [True, True]:
            print("deadlock")
            return sent
        ins, data = prog[pc[cpu]]
        jmp = 1
        if ins == 'snd':
            if cpu == 1:
                sent += 1
            freq = val(cpu,data[0])
            queue[1-cpu].append(val(cpu,data[0]))
            waiting[1-cpu] = False
        elif ins == 'set':
            regs[(cpu,data[0])] = val(cpu,data[1])
        elif ins == 'add':
            regs[(cpu,data[0])] += val(cpu,data[1])
        elif ins == 'mul':
            regs[(cpu,data[0])] *= val(cpu,data[1])
        elif ins == 'mod':
            regs[(cpu,data[0])] %= val(cpu,data[1])
        elif ins == 'rcv':
            if queue[cpu] != []:
                regs[(cpu,data[0])] = queue[cpu].pop(0)
            else:
                waiting[cpu] = True
                cpu = 1-cpu
#                print(cpu)
                jmp = 0
        elif ins == 'jgz':
            if val(cpu,data[0]):
                jmp = val(cpu,data[1])
        pc[cpu] += jmp

print(sndchip(inputstring))

