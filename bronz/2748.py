n = int(input())
sum = [0,1]

for i in range(2, n+1):
    sum.append(sum[i-2]+sum[i-1])
    
print(sum[n])