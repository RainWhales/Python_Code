import sys

A = [x for x in range(1, 31)]

for i in range(28):
    S = int(sys.stdin.readline())
    A.remove(S)

print(min(A))
print(max(A))
