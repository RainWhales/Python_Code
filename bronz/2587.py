import sys

Nums = [int(sys.stdin.readline()) for _ in range(5)]
Nums.sort()
print(f'{int(sum(Nums)/len(Nums))}')
print(Nums[2])