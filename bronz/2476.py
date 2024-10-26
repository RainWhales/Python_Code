import sys

people = int(input())
dicePrice = []

for j in range(people):
    diceNumber = list(map(int, sys.stdin.readline().split()))

    if diceNumber[0] == diceNumber[1] == diceNumber[2]:
        dicePrice.append(10000 + diceNumber[0]*1000)
    
    elif diceNumber[0] == diceNumber[1] != diceNumber[2]:
        dicePrice.append(1000 + diceNumber[0]*100)
    
    elif diceNumber[0] == diceNumber[2] != diceNumber[1]:
        dicePrice.append(1000 + diceNumber[0]*100)
    
    elif diceNumber[1] == diceNumber[2] != diceNumber[0]:
        dicePrice.append(1000 + diceNumber[1]*100)
        
    elif diceNumber[0] != diceNumber[1] != diceNumber[2]:
        dicePrice.append(max(diceNumber)*100)
        
print(max(dicePrice))