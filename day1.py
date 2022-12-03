import csv

def countCalories(elvesInventory : list) -> str:
    elfRanking = []
    elfCounter = 0
    elfRanking.append(0)
    for indx in range(len(elvesInventory)):
        if elvesInventory[indx] == " ":
            elfCounter += 1
            elfRanking.append(0)
        else:
            elfRanking[elfCounter] += int(elvesInventory[indx])
    return elfRanking

inventoryTest = [1000, 2000, 3000,"", 4000, "", 5000, 6000, "", 7000, 8000, 9000, "",10000]

inventory = []

default = " "

with open('InputDay1.csv') as f:
    readCsv = csv.reader(f)
    for zeile in readCsv:
        if zeile == []:
            inventory.append(default)
        else:
            inventory.append(zeile[0])

print(type(inventory))

elfCalories = countCalories(inventory)

print(f"The top elf carries {max(elfCalories)} calories in total.")

maxthree = 0

for x in range(1, 4):
    maxthree = maxthree + sorted(elfCalories)[-x]

# print(a)

# maxthree = sorted(elfCalories)[-1] + sorted(elfCalories)[-2] +sorted(elfCalories)[-3]

print(f"The top three Elves carry {maxthree} calories in total.")