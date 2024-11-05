import sys

N, M = map(int, input().split())

Bucket = [ x for x in range(1,N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    Bucket[a-1] , Bucket[b-1] = Bucket[b-1], Bucket[a-1]

print(' '.join(map(str, Bucket)))
