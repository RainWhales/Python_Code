import sys

def Rev(x):
    Revs = ''
    for i in x:
        Revs = i + Revs
    return Revs

while True:
    A = sys.stdin.readline().rstrip()
    if A == 'END':
        break
    print(Rev(A))