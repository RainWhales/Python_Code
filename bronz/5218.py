import sys

T = int(input())

Ap = [chr(i) for i in range(ord('A'), ord('Z')+1)]
Ip_Alpa = [sys.stdin.readline().split() for _ in range(T)]

print(Ap)
print(Ip_Alpa)