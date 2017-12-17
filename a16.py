def input_string(day):
    filename = "advent{}.txt".format(day)
    with open(filename, 'r') as myfile:
        return myfile.read()

inputstring = input_string(16).strip()
danced = {}

def dance(st, line = 'abcdefghijklmnop'):
    for move in st.split(','):
        if move[0] == 's':
            n = int(move[1:])
            line = line[-n:] + line[0:-n]
        elif move[0] == 'x':
            m, n = (int(z) for z in move[1:].split('/'))
            tline = list(line)
            tline[m], tline[n] = tline[n], tline[m]
            line = ''.join(tline)
        elif move[0] == 'p':
            m, n = move[1:].split('/')
            line = line.replace(m, '.').replace(n, m).replace('.', n)
    return(line)

line = 'abcdefghijklmnop'
for i in range(1000000000 % 60):  # human loop detector notes that the dance has period 60
    if line in danced:
#        print("loop!", i, line)
        outline = danced[line]
    else:
        outline = dance(inputstring, line)
        danced[line] = outline
    line = outline
print(line)


