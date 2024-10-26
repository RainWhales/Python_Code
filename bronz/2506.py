N = int(input())
l = list(map(int, input().split()))
sum = 0
a = 0

for i in l:
    if i == 1:
        a += 1
        sum += a
    else:
        a = 0
        
print(sum)