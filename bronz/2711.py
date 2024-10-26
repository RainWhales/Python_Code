import sys

T = int(input())

StrList = [sys.stdin.readline().split() for x in range(T)]

for i in StrList:
    n = int(i[0])
    StrList_Result = i[1][:(n-1)]+i[1][(n):]
    print(StrList_Result)
