import Default.adventofcode as aof

# IMPORT DATA
splitter = "\n"

# data = aof.getDayData_int(6, splitter)
data = aof.getDayData_str(6, splitter)

print("Data:", data)

# PART ONE
DISTINCTCHAR = 4

for i in range(len(data[0])):
    tmp = set()

    for letter in data[0][i:i + DISTINCTCHAR]:
        tmp.add(letter)

    if len(tmp) == DISTINCTCHAR:
        erg = i + DISTINCTCHAR
        break

ans = erg

aof.answer(ans, 6, 1)

# PART TWO
DISTINCTCHAR = 14

for i in range(len(data[0])):
    tmp = set()

    for letter in data[0][i:i + DISTINCTCHAR]:
        tmp.add(letter)

    if len(tmp) == DISTINCTCHAR:
        erg = i + DISTINCTCHAR
        break

ans = erg

aof.answer(ans, 6, 2)
