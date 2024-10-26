N, K = map(int, input().split())

def Yak(x):
    Y = []
    for i in range(1,x+1):
        if x % i == 0:
            Y.append(i)
            
    return Y

Ya = sorted(Yak(N))

if len(Ya) < K:
    print(0)
else:
    print(Ya[K-1])