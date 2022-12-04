import Default.adventofcode as aof

# IMPORT DATA
splitter = "\n"

# data = aof.getDayData_int(4, splitter)
data = aof.getDayData_str(4, splitter)

print("Data:", data)

# PART ONE
erg = 0 # test

for i_elf in range(len(data)):
    elf = data[i_elf].split(",")
    first_elf = list(map(int, elf[0].split("-")))
    second_elf = list(map(int, elf[1].split("-")))

    if second_elf[0] >= first_elf[0] and second_elf[1] <= first_elf[1]:
        erg += 1
    elif first_elf[0] >= second_elf[0] and first_elf[1] <= second_elf[1]:
        erg += 1

ans = erg

aof.answer(ans, 4, 1)

# PART TWO
erg = 0

for i_elf in range(len(data)):
    elf = data[i_elf].split(",")
    first_elf = list(map(int, elf[0].split("-")))
    second_elf = list(map(int, elf[1].split("-")))

    if sum(first_elf) > sum(second_elf):
        first_list = first_elf
        second_list = second_elf

    else:
        first_list = second_elf
        second_list = first_elf

    for num in range(first_list[0], first_list[1] + 1):
        check = False
        for num2 in range(second_list[0], second_list[1] + 1):
            if num == num2:
                erg += 1
                check = True
                break

        if check:
            break

ans = erg

aof.answer(ans, 4, 2)
