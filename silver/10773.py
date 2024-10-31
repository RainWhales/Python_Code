import sys

T = int(input())
Nums = []

for n in range(T):
    ip = int(sys.stdin.readline())
    if ip != 0:
        Nums.append(ip)
    else:
        Nums.pop()
        
print(sum(Nums))

