S = input()
N = 0
C = ['c=','c-','dz=','d-','lj','nj','s=','z=']
CS = []

for i in C:
    if i in S:
        S = S.replace(i, '*')
        
N += len(S)
        
        
(print(N))