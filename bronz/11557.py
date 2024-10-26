import sys

TCase = int(input())

Sake = {}

for i in range(TCase):
    SNum = int(input())
    for j in range(SNum):
        a, b = sys.stdin.readline().split()
        Sake[a] = int(b)
        name = max(Sake, key = Sake.get)
    Sake = {}
    print(name)

