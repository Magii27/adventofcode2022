import Default.adventofcode as aof

# IMPORT DATA
splitter = "\n\n"

# data = aof.getDayData_int(1, splitter)
data = aof.getDayData_str(1, splitter)

print("Data:", data)

# PART ON

high_val = 0

for elf in data:
    elf_data = sum(list(map(int, elf.split("\n"))))
    if elf_data > high_val:
        high_val = elf_data

ans = high_val

aof.answer(ans, 1, 1)

# PART TWO

high_val = [0, 0, 0]

for elf in data:
    elf_data = sum(list(map(int, elf.split("\n"))))
    for i, high in enumerate(high_val):
        if elf_data > high:
            high_val.insert(i, elf_data)
            high_val.pop()
            break

ans = sum(high_val)

aof.answer(ans, 1, 2)
