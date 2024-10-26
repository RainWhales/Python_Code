import sys

Nums = [int(sys.stdin.readline())%42 for _ in range(10)]
R = []
for i in Nums:
    R.append(i)
    
a = set(R)

print(len(a))