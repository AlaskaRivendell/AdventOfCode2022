import csv

def countCalories(elvesInventory : list) -> str:
    elfRanking = []
    elfCounter = 0
    elfRanking.append(0)
    for indx in range(len(elvesInventory)):
        if elvesInventory[indx][0] == " ":
            elfCounter += 1
            elfRanking.append(0)
        else:
            elfRanking[elfCounter] += int(elvesInventory[indx][0])
    return elfRanking

inventoryTest = [1000, 2000, 3000,"", 4000, "", 5000, 6000, "", 7000, 8000, 9000, "",10000]

# inputDay1 = open("InputDay1.txt", "r")

inventory = []

default = " "

with open('InputDay1.csv') as f:
    readCsv = csv.reader(f)
    for zeile in readCsv:
        if zeile == []:
            inventory.append(default)
        else:
            inventory.append(zeile)

print(type(inventory))


print(countCalories(inventory))