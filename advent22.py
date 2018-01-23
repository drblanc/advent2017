inp = """.#...#.#.##..##....##.#.#
###.###..##...##.##....##
....#.###..#...#####..#.#
.##.######..###.##..#...#
#..#..#..##..###...#..###
..####...#.##.#.#.##.####
#......#..####..###..###.
#####.##.#.#.##.###.#.#.#
.#.###....###....##....##
.......########.#.#...#..
...###.####.##..###.##..#
#.#.###.####.###.###.###.
.######...###.....#......
....##.###..#.#.###...##.
#.###..###.#.#.##.#.##.##
#.#.#..###...###.###.....
##..##.##...##.##..##.#.#
.....##......##..#.##...#
..##.#.###.#...#####.#.##
....##..#.#.#.#..###.#..#
###..##.##....##.#....##.
#..####...####.#.##..#.##
####.###...####..##.#.#.#
#.#.#.###.....###.##.###.
.#...##.#.##..###.#.###.."""

sample = """..#
#..
..."""

from collections import defaultdict

def turnright(dx, dy):
    return (-dy, dx)

def turnleft(dx, dy):
    return (dy, -dx)

def drawmap(grid):
    xvals = []
    yvals = []
    for y,x in grid.keys():
        xvals.append(x)
        yvals.append(y)
    xmin, xmax = min(xvals), max(xvals)
    ymin, ymax = min(yvals), max(yvals)
    for y in range(ymin,ymax+1):
        line = []
        for x in range(xmin, xmax+1):
            if grid.get((y,x), False):
                line.append('#')
            else:
                line.append('.')
        print(''.join(line))

def infect(init, n = 70):
    grid = {}
    txtgrid = init.splitlines()
    for y in range(len(txtgrid)):
        for x in range(len(txtgrid[y])):
            if txtgrid[y][x] == '#':
                grid[(y,x)] = True
    dim = len(txtgrid) // 2
    x, y = dim, dim
    dx, dy = 0, -1
    burst = 0
    for _ in range(n):
        if grid.get((y,x), False):
            dx, dy = turnright(dx, dy)
            grid[(y,x)] = False
        else:
            dx, dy = turnleft(dx, dy)
            burst += 1
            grid[(y,x)] = True
        x += dx
        y += dy

    dx, dy = 0, -1
    return burst

def infect2(init, n = 70):
    grid = {}
    txtgrid = init.splitlines()
    for y in range(len(txtgrid)):
        for x in range(len(txtgrid[y])):
            if txtgrid[y][x] == '#':
                grid[(y,x)] = '#'
    dim = len(txtgrid) // 2
    x, y = dim, dim
    dx, dy = 0, -1
    burst = 0
    for _ in range(n):
        cellstate = grid.get((y,x), '.')
        if cellstate == '.':
            dx, dy = turnleft(dx, dy)
            grid[(y,x)] = 'W'
        elif cellstate == 'W':
            grid[(y,x)] = '#'
            burst += 1
        elif cellstate == '#':
            dx, dy = turnright(dx, dy)
            grid[(y,x)] = 'F'
        elif cellstate == 'F':
            dx, dy = -dx, -dy
            grid[(y,x)] = '.'
        x += dx
        y += dy

    dx, dy = 0, -1
    return burst

print(infect2(inp,10000000))

