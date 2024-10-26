N = int(input())
sum = 0

for i in range(N+1):
    for j in range(i+1):
        sum += j
        sum += i
        
print(sum)