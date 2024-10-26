import sys

Num = [int(sys.stdin.readline()) for x in range(3)]
arr = 1

for i in Num:
    arr *= i

arr_s = str(arr)

for j in range(10):
    print(arr_s.count(str(j)))