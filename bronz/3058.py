T = int(input())

for i in range(T):
    Nums = list(map(int, input().split()))
    even = []
    for j in Nums:
        if j % 2 == 0:
           even.append(j) 
    print(sum(even),min(even))