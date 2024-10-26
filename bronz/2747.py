FV = [0,1]
N = int(input())

[FV.append(FV[x-2]+FV[x-1]) for x in range(2, N+1)]

print(FV[N])