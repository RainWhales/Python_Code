import sys

W = [int(sys.stdin.readline()) for _ in range(10)]
K = [int(sys.stdin.readline()) for _ in range(10)]
W.sort(reverse=True)
K.sort(reverse=True)

print(sum(W[:3]), sum(K[:3]))
