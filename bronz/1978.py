N = int(input())
dem = list(map(int, input().split()))
sum = 0

def demical(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0 :
            return False

    return True

for j in dem:
    R = demical(j)
    if R:
        sum += 1
        
print(sum)