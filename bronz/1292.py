a ,b = map(int, (input().split()))
S1 = 0

N = []
for i in range(1, b+1):
    if len(N) >=b:
        break
    for j in range(i):
        if len(N) < b:
            N.append(i)
        else:
            break  
print(N)
print(sum(N[a-1:b]))