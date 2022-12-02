import Default.adventofcode as aof

# IMPORT DATA
splitter = "\n"

# data = aof.getDayData_int(2, splitter)
data = aof.getDayData_str(2, splitter)

print("Data:", data)

elf_rules = {"A":"R", "B":"P", "C":"S"}
player_rules = {"X":"R", "Y":"P", "Z":"S"}

rules = {"R": "S", "P": "R", "S": "P"}
points = {"R": 1, "P": 2, "S": 3}

# PART ONE
erg = 0
for gameround in data:
    elf = elf_rules[gameround[:gameround.find(" ")]]
    player = player_rules[gameround[gameround.find(" ") + 1:]]
    if rules[elf] == player:
        erg += points[player]
    elif rules[player] == elf:
        erg += points[player] + 6
    else:
        erg += points[player] + 3


ans = erg

aof.answer(ans, 2, 1)

# PART TWO
rules_lose = {"S": "R", "R": "P", "P": "S"}
rules_win = {"R": "S", "P": "R", "S": "P"}

erg = 0

for gameround in data:
    elf = elf_rules[gameround[:gameround.find(" ")]]
    player_input = gameround[gameround.find(" ") + 1:]
    player = player_rules[player_input]

    if player_input == "X":
        erg += points[rules_win[elf]]
    elif player_input == "Y":
        erg += points[elf] + 3
    else:
        erg += points[rules_lose[elf]] + 6


ans = erg

aof.answer(ans, 2, 2)
