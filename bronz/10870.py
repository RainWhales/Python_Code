N = int(input())
piv = []
for i in range(N+1):
    if i == 0:
        piv.append(0)
    elif i == 1:
        piv.append(1)
    else:
        piv.append(piv[i-2]+piv[i-1])

print(piv[N])