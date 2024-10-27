a ,b = map(int, (input().split()))
S1 = 0
S_count = 0
for i in range(1,b+1):
    for j in range(0, i):
        S_count += 1
        if a <= S_count <= b:
            S1 += i
        if S_count == b:
            break
    
    if S_count == b:
        break
    
print(S1)
    














# N = []
# for i in range(1, b+1):
#     if len(N) >=b:
#         break
#     for j in range(i):
#         if len(N) < b:
#             N.append(i)
#         else:
#             break  
# print(N)
# print(sum(N[a-1:b]))