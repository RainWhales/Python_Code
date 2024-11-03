N = int(input())
a = 1
for i in range(1,N+1):
    a *= i
    
a = ''.join(reversed(str(a)))
cnt = 0

for j in a:
    if j == '0':
        cnt += 1
    else:
        break

print(cnt)