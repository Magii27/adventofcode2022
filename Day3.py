import Default.adventofcode as aof
import string

# IMPORT DATA
splitter = "\n"

# data = aof.getDayData_int(3, splitter)
data = aof.getDayData_str(3, splitter)

print("Data:", data)

# PART ONE

listofletters = list(string.ascii_letters)

print(listofletters)
erg = 0
for item in data:
    first_item = item[len(item)//2:]
    second_item = item[:len(item)//2]
    for letter_first in first_item:
        if letter_first in second_item:
            erg += listofletters.index(letter_first) + 1
            break

ans = erg

aof.answer(ans, 3, 1)

# PART TWO
erg = 0
group = []

count = 0

for i, item in enumerate(data):
    if count > 0:
        count -= 1
        continue
    count += 2

    group = [data[i], data[i+1], data[i+2]]

    for letters_i in data[i]:
        if data[i+1].count(letters_i) >= 1 and data[i+2].count(letters_i) >= 1:
            erg += listofletters.index(letters_i) + 1
            break

    #print(group)
    #found = False
    #letters = []
    #count_letter = []
    #for i_group in range(len(group)):
    #    for letter in group[i_group]:
    #        if not letter in letters and i_group == 0:
    #            letters.append(letter)
    #            count_letter.append(1)
    #        else:
    #            print(letter)
    #            print(letters)
    #            print(count_letter)
    #            count_letter[letters.index(letter)] += 1
    #print(count_letter)
    #print(letters)
    #print(count_letter.index(3))
    #erg += listofletters.index(letters[count_letter.index(3)])

ans = erg

aof.answer(ans, 3, 2)
