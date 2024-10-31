import sys

Nums = [int(sys.stdin.readline()) for _ in range(9)]

for i in Nums:
    for j in Nums:
        if i == j:
            continue
        else:
            if sum(Nums) - (i+j) == 100:
                Nums.remove(i)
                Nums.remove(j)
                for c in Nums:
                    print(c)
