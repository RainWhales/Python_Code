import sys

Nums = [int(sys.stdin.readline()) for x in range(7)]
Num_odd = [x for x in Nums if x%2 != 0]
Num_odd.sort()

if not Num_odd:
    print(-1)
else:
    print(sum(Num_odd))
    print(Num_odd[0])