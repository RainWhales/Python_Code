import sys

Total_cost = int(input())
Total_case = int(input())
cost = 0
for i in range(Total_case):
    a, b = map(int, sys.stdin.readline().split())
    cost += (a*b)
    
if cost == Total_cost:
    print('Yes')
else:
    print('No')