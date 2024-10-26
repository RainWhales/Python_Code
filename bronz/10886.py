import sys

Number = int(input())
Vote = []

for i in range(Number):
    Vote.append(int(sys.stdin.readline().strip()))

if Vote.count(1) > Vote.count(0):
    print('Junhee is cute!')
elif Vote.count(1) < Vote.count(0):
    print('Junhee is not cute!')