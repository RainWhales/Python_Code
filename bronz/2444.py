T = int(input())

for i in range(1, T+1):
    print(' '*(T-i)+'*'*(2*i-1))
for j in range(1, T):
    print(' '*j+'*'*(2*(T-j)-1))