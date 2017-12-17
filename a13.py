def input_string(day):
    filename = "advent{}.txt".format(day)
    with open(filename, 'r') as myfile:
        return myfile.read()

def safepass(istring):
    fw = {}
    for l in istring.split('\n'):
        n, d = l.split(':')
        fw[int(n)] = int(d)
    last = max(fw.keys())

    def safe(delay):
        sev = 0
        for l in range(last+1):
            if l in fw:
                if (l+delay)%(2*(fw[l]-1)) == 0:
                    return False
        return True

    d = 0
    while True:
        if safe(d):
            print(d, "is safe")
            return
        d += 1

safepass(input_string(13))

