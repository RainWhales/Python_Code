import sys


SmallM = [int(sys.stdin.readline()) for _ in range(9)]
Sum = sum(SmallM)

for i in range(9):
    for j in range(i+1, 9):
        if Sum - (SmallM[i]+SmallM[j]) == 100:
            del SmallM[j]
            del SmallM[i]
            SmallM.sort()
            for c in SmallM:
                print(c)
            exit()
            