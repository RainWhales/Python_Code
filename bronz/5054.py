import sys
T = int(input())

for _ in range(T):
    n = int(input())
    location = list(map(int, sys.stdin.readline().split()))
    location.sort()
   
    print(f"{(max(location)-min(location))*2}")