import Default.adventofcode as aof

# IMPORT DATA
splitter = "\n\n"

# data = aof.getDayData_int(5, splitter)
data = aof.getDayData_str(5, splitter)

print("Data:", data)

# PART ONE
data_start = data[0].split("\n")
data_start = data_start[len(data_start) - 1].replace(" ", "")

data_dict = {}
for num in data_start:
    data_dict[int(num)] = []


for index, item in enumerate(data[0].split("\n")):
    i = 1
    if index == len(data[0].split("\n")) - 1:
        break
    for i_item in range(1, len(item), 4):
        if item[i_item] == " ":
            i += 1
            continue

        data_dict[i].insert(0, item[i_item])
        i += 1


data_moves = data[1].split("\n")
for moving in data_moves:
    tmp = moving.split(" ")
    many = int(tmp[1])
    src = int(tmp[3])
    des = int(tmp[5])

    tmp = []
    for round in range(many):
        tmp.append(data_dict[src][len(data_dict[src]) - 1])
        data_dict[src].pop()

    for item in tmp:
        data_dict[des].append(item)

erg = ""

for key in data_dict:
    erg += data_dict[key][len(data_dict[key]) - 1]

ans = erg

aof.answer(ans, 5, 1)

# PART TWO
data_dict = {}
for num in data_start:
    data_dict[int(num)] = []


for index, item in enumerate(data[0].split("\n")):
    i = 1
    if index == len(data[0].split("\n")) - 1:
        break
    for i_item in range(1, len(item), 4):
        if item[i_item] == " ":
            i += 1
            continue

        data_dict[i].insert(0, item[i_item])
        i += 1

data_moves = data[1].split("\n")
for moving in data_moves:
    tmp = moving.split(" ")
    many = int(tmp[1])
    src = int(tmp[3])
    des = int(tmp[5])

    tmp = []

    for round in range(many):
        tmp.append(data_dict[src][len(data_dict[src]) - many + round])
        data_dict[src].pop(len(data_dict[src]) - many + round)

    for item in tmp:
        data_dict[des].append(item)

erg = ""

for key in data_dict:
    erg += data_dict[key][len(data_dict[key]) - 1]

ans = erg

aof.answer(ans, 5, 2)
