
M = int(input())
N = int(input())
dem = []

def demical(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
        
    return True
    
for j in range(M, N+1):
    R = demical(j)
    if R:
        dem.append(j)
        
if not dem:
    print(-1)
else:
    print(sum(dem))
    print(min(dem))