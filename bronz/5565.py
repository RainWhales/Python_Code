import sys

Total = int(input())
a = []

for i in range(9):
    a.append(int(sys.stdin.readline()))
    
print(Total - sum(a))