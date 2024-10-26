import sys

T = int(input())

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(f"You get {a//b} piece(s) and your dad gets {a%b} piece(s).")