import Default.adventofcode as aof

# IMPORT DATA
splitter = "\n"

# data = aof.getDayData_int(8, splitter)
data = aof.getDayData_str(8, splitter)

print("Data:", data)


# PART ONE
def check(array):
    pass


forest = [list(map(int, tree)) for tree in data]
visible = [[False for j in range(len(data[0]))] for i in range(len(data))]

erg = 0

for y in range(len(forest)):
    highestx = 0
    for x in range(len(forest[0])):
        if x in (0, len(forest[0]) - 1) or y in (0, len(forest) - 1):
            visible[y][x] = True
            highestx = forest[y][x]
        else:
            if forest[y][x] > highestx:
                highestx = forest[y][x]
                visible[y][x] = True

    for x in range(len(forest[0]) - 1, 0, -1):
        if x in (0, len(forest[0]) - 1) or y in (0, len(forest) - 1):
            visible[y][x] = True
            highestx = forest[y][x]
        else:
            if forest[y][x] > highestx:
                highestx = forest[y][x]
                visible[y][x] = True

for x in range(len(forest[0])):
    highesty = 0
    for y in range(len(forest)):
        if x in (0, len(forest[0]) - 1) or y in (0, len(forest) - 1):
            visible[y][x] = True
            highesty = forest[y][x]
        else:
            if forest[y][x] > highesty:
                highesty = forest[y][x]
                visible[y][x] = True

    for y in range(len(forest) - 1, 0, -1):
        if x in (0, len(forest[0]) - 1) or y in (0, len(forest) - 1):
            visible[y][x] = True
            highesty = forest[y][x]
        else:
            if forest[y][x] > highesty:
                highesty = forest[y][x]
                visible[y][x] = True

erg = sum([i.count(True) for i in visible])

ans = erg

aof.answer(ans, 8, 1)

# PART TWO
highest = 0



def left(y, x, last_highest):
    global forest

    if x == 0:
        if forest[y][x] > last_highest:
            return 1
        else:
            return 0
    if forest[y][x] > last_highest:
        last_highest = forest[y][x]
        return 1 + left(y, x - 1, last_highest)
    else:
        return 1 + left(y, x - 1, last_highest)


def right(y, x, last_highest):
    global forest

    if x == len(forest[0]) - 1:
        if forest[y][x] > last_highest:
            return 1
        else:
            return 0
    if forest[y][x] > last_highest:
        last_highest = forest[y][x]
        return 1 + right(y, x + 1, last_highest)
    else:
        return 1 + right(y, x + 1, forest[y][x])


def up(y, x, last_highest):
    global forest
    if y == 0:
        if forest[y][x] > last_highest:
            return 1
        else:
            return 0
    if forest[y][x] > last_highest:
        last_highest = forest[y][x]
        return 1 + up(y - 1, x, last_highest)
    else:
        return 1 + up(y - 1, x, last_highest)


def down(y, x, last_highest):
    global forest
    if y == len(forest) - 1:
        if forest[y][x] > last_highest:
            return 1
        else:
            return 0
    if forest[y][x] > last_highest:
        last_highest = forest[y][x]
        return 1 + down(y + 1, x, last_highest)
    else:
        return 1 + down(y + 1, x, last_highest)


for y in range(len(forest)):
    for x in range(len(forest[0])):
        print(forest[y][x])
        print(y, x)
        cleft, cright, cup, cdown = 1, 1, 1, 1
        if y == 0:
            if x == 0:
                cdown = down(y + 1, x, 0)
                cright = right(y, x + 1, 0)
            elif x == len(forest[0]) - 1:
                cleft = left(y, x - 1, 0)
                cdown = down(y + 1, x, 0)
            else:
                cdown = down(y + 1, x, 0)
                cleft = left(y, x - 1, 0)
                cright = right(y, x + 1, 0)
        elif y == len(forest) - 1:
            if x == 0:
                cright = right(y, x + 1, 0)
                cup = up(y - 1, x, 0)
            elif x == len(forest[0]) - 1:
                cleft = left(y, x - 1, 0)
                cup = up(y - 1, x, 0)
            else:
                cup = up(y - 1, x, 0)
                cleft = left(y, x - 1, 0)
                cright = right(y, x + 1, 0)
        else:
            if x == 0:
                cdown = down(y + 1, x, 0)
                cright = right(y, x + 1, 0)
                cup = up(y - 1, x, 0)
            elif x == len(forest[0]) - 1:
                cleft = left(y, x - 1, 0)
                cdown = down(y + 1, x, 0)
                cup = up(y - 1, x, 0)
            else:
                cup = up(y - 1, x, 0)
                cdown = down(y + 1, x, 0)
                cleft = left(y, x - 1, 0)
                cright = right(y, x + 1, 0)

        tmp = cleft * cright * cdown * cup
#
        print(cleft , cright , cup , cdown)
        if tmp > highest:
            highest = tmp

ans = highest
# 474606

aof.answer(ans, 8, 2)
